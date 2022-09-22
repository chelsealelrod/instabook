"""View module for handling requests about posts"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from instabookapi.models import Post, InstaBookUser
from django.contrib.auth import get_user_model
User = get_user_model()

class PostView(ViewSet):
    """User posts"""

    def list(self, request):
        """Handle GET requests to posts resource

        Returns:
            Response -- JSON serialized list of posts
        """
        # Get all comment records from the database
        posts = Post.objects.all()

        # Support filtering comments by type
        #    http://localhost:8000/comments?type=1
        #
        post_type = self.request.query_params.get('type', None)
        if post_type is not None:
            posts = posts.filter(post_type__id=post_type)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/posts/2
            #
            # The `2` at the end of the route becomes `pk`
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized a post instance
        """
        
        # Uses the token passed in the `Authorization` header
        instabookuser = InstaBookUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["commentId"])
        post = Post()
        post.instabookuser = instabookuser
        post.image = request.data["image"]
        post.content = request.data["content"]
        post.publish = request.data["publish"]
        
        
        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
       
   
    def update(self, request, pk=None):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
        instabookuser = InstaBookUser.objects.get(user=request.auth.user)

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Comment, get the comment record
        # from the database whose primary key is `pk`
        post = Post.objects.get(pk=pk)
        post.instabookuser = instabookuser
        post.image = request.data["image"]
        post.content = request.data["content"]
        post.amount_due = request.data["publish"]
        post.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

   
class PostSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post
        fields = ('id','instabookuser', 'image', 'content',
                  'publish')
        depth = 1

class PostUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class InstaBookUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = PostUserSerializer(many=False)

    class Meta:
        model = InstaBookUser
        fields = ('id', 'user', 'bio', 'imageURL', 'location', 'created_on')