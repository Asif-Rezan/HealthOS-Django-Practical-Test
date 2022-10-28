from django.contrib import admin
from .models import Subscription, UpdateSubscriptionTrack, UserInfo
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Subscription)
admin.site.register(UpdateSubscriptionTrack)