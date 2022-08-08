from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    imageURL = models.ImageField(blank=True, upload_to='bio_image')
    location = models.CharField(max_length=20)