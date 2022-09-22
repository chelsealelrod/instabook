from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
# from .instabookuser import InstaBookUser


class Post(models.Model):
    # instabookuser = models.ForeignKey(
    #     InstaBookUser, verbose_name="InstaBookUser",
    #     null=True,
    #     on_delete=models.SET_NULL)
    title = models.CharField(max_length=300, default=None)
    image = models.ImageField(blank=True, upload_to='post_images')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)