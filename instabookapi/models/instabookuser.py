from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class InstaBookUser(models.Model):
    
    user = models.OneToOneField(User,
            on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, null=True)
    imageURL = models.URLField(null=True, max_length=500)
    location = models.CharField(max_length=100, null=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "instabook"  