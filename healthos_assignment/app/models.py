from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(AbstractUser):
    phoneNumber = models.CharField(max_length=15)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username= models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=250)
    password1 = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)



    
