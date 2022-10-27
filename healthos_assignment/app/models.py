from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class UserInfo(AbstractUser):
    phoneNumber = models.CharField(max_length=15)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username= models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=250)
    password1 = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)


class Subscription(models.Model):
    user=models.OneToOneField(UserInfo, on_delete=CASCADE,primary_key=True)
    subscription_type = models.CharField(max_length = 50, null= True)
    




    
