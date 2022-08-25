"""View module for handling requests about comments"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from instabookapi.models import Comment, InstaBookUser
from django.contrib.auth import get_user_model
User = get_user_model()

class CommentView(ViewSet):
    """Comment posts"""

    def list(self, request):
        """Handle GET requests to comments resource

        Returns:
            Response -- JSON serialized list of comments
        """
        # Get all comment records from the database
        comments = Comment.objects.all()

        # Support filtering comments by type
        #    http://localhost:8000/comments?type=1
        #
        comment_type = self.request.query_params.get('type', None)
        if comment_type is not None:
            comments = comments.filter(bill_type__id=comment_type)

        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized post instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/comments/2
            #
            # The `2` at the end of the route becomes `pk`
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
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
        comment = Comment.objects.get(pk=request.data["commentId"])
        comment = Comment()
        comment.instabookuser = instabookuser
        comment.image = request.data["image"]
        comment.content = request.data["content"]
        comment.publish = request.data["publish"]
        
        
        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
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
        comment = Comment.objects.get(pk=pk)
        comment.instabookuser = instabookuser
        comment.image = request.data["image"]
        comment.content = request.data["content"]
        comment.amount_due = request.data["publish"]
        comment.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

   
class CommentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = ('id','instabookuser', 'image', 'content',
                  'publish')
        depth = 1

class CommentUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class InstaBookUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = CommentUserSerializer(many=False)

    class Meta:
        model = InstaBookUser
        fields = ['user']