from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Profile(models.Model):
    
    instabookuser = models.ForeignKey("instabookapi.instabookuser",
            on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=50)
    imageURL = models.ImageField(blank=True, upload_to='bio_image')
    location = models.CharField(max_length=20)