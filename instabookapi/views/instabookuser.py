from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class InstaBookUser(ViewSet):
    

    def list(self, request):
        """
        Get InstaBookUser
        """
        instabookuser = request.auth.user.instabookuser
            
        serializer = InstaBookUserSerializer(instabookuser, context={'request': request})
            
        return Response(serializer.data)
    
        
class InstaBookUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""

    class Meta:
        model = InstaBookUser
        fields = ('id', 'user', 'bio', 'imageURL', 'location', 'created_on')