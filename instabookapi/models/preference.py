from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from .post import Post


class Preference(models.Model):
    user= models.ForeignKey(User, verbose_name="User", null=True,
        on_delete=models.SET_NULL)
    post= models.ForeignKey(Post, verbose_name="Post", null=True,
        on_delete=models.SET_NULL)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    
    # def __str__(self):
    #     return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    # class Meta:
    #    unique_together = ("user", "post", "value")