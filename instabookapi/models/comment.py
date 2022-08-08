from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):

    user = models.OneToOneField(User,
          on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='post_images')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)