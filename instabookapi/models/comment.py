from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
# from .instabookuser import InstaBookUser


class Comment(models.Model):
#     instabookuser = models.ForeignKey(
#         InstaBookUser, verbose_name="InstaBookUser",
#         null=True,
#         on_delete=models.SET_NULL)
    image = models.ImageField(blank=True, upload_to='post_images')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)