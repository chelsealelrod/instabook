from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from instabookapi.models import InstaBookUser


@api_view( ['GET'])
def get_instabookuser_profile(request):
    """
    Get InstaBookUser
    """
    instabookuser = request.auth.user.instabookuser
        
    serializer = InstaBookUserSerializer(instabookuser, context={'request': request})
        
    return Response(serializer.data)
    

class InstaBookUserSerializer(serializers.ModelSerializer):
    """
    InstaBookUser
    """
    
    class Meta:
        model = InstaBookUser
        fields = ('user')
        
        