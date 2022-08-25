from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=300, default=None)
    image = models.ImageField(blank=True, upload_to='post_images')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)