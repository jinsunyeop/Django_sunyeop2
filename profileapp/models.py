from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(max_length=10,unique=True,null=True,verbose_name='사진을 올려보거라')
    nickname = models.CharField(max_length=10,unique=True,null=False)
    message = models.CharField(max_length=30,null=True)

