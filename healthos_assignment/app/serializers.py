from rest_framework.serializers import ModelSerializer
from .models import UserInfo
from django.contrib.auth import models

class userSeriliazer(ModelSerializer):
  class Meta:
    model= UserInfo
    fields= '__all__'