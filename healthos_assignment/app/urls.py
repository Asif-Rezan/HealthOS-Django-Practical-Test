from . import views
from django.urls import path



urlpatterns = [
    path('registration/',views.UserRegistration,name='registration'),
    path('get-unsubcribed-user-number/',views.getUnsubcribedUserPhoneNumber,name='get_user_number'),
    path('subscribe/<str:type>/',views.SubscribeUser,name='subscribe'),
    path('update-subscription/<str:type>/',views.updateSubscription,name='update-subscription'),
    path('make-payment/', views.MakePaymentSession.as_view())

    
]