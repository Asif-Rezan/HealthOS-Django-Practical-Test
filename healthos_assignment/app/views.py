from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UpdateSubscriptionTrack, UserInfo, Subscription
from random import randint
from .serializers import userSeriliazer
from datetime import datetime  
from datetime import timedelta 
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


@api_view(['GET','POST'])
def UserRegistration(request):

  # get user info------------->>>
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    

    # validate and assign phone number start -------->>>>>>

    range_start = 10**(8-1)   
    range_end = (10**8)-1
    rand_number = randint(range_start, range_end)  #random last 8 digit number
    rand_number = str(rand_number)
    country_code = '+88'
    phn_operator_code = ['017','016','019','015','018']
    rand_operator_code = phn_operator_code[randint(0,4)] 
    phoneNumber = country_code + rand_operator_code + rand_number  #assign a phone number
    #print('Phone number ...',phoneNumber)

   #  validate and assign phone number end ------>>>>>>>>>>




  # Save user info
    user_data = UserInfo(
      first_name = first_name,
      last_name = last_name,
      username = username,
      email = email,
      password1 = password1,
      password2 = password2,
      phoneNumber = phoneNumber
    )
    user_data.save()



  return Response("Saved data")




#  Get the users phone number if they are not subscribed
@api_view(['GET'])
def getUnsubcribedUserPhoneNumber(request):
  unsubcribed_user_info = UserInfo.objects.filter(subscription__subscription_type__contains= '')
  user_serializer= userSeriliazer(unsubcribed_user_info, many=True)
  return Response(user_serializer.data)






# Customer subscription start ------------------>>>

@api_view(['GET','POST'])
def SubscribeUser(request,type):

  print(request.user)
  
  if(type == 'Silver' or type == 'Bronze'):

      Subscription.objects.create(
      user=request.user,
      subscription_type= type,
      subscription_end_time = datetime.now() + timedelta(days=365)

    )
  elif(type=='Gold'):
      
      end_date = None

      Subscription.objects.create(
      user=request.user,
      subscription_type='Gold',
      subscription_end_time = end_date

    )
  
  else:
    return Response('Something is wrong! please try again!')

    
  
  return Response('Subscription Successfull')

# Customer subscription end ------------------>>>





#Update customer subscription and track
@api_view(['GET','PUT','POST'])
def updateSubscription(request,type):
  user = request.user
  try:
    privious_subscription_plan= Subscription.objects.get(user=user)
  except:
    privious_subscription_plan = None

  if(type == 'Silver' or type == 'Bronze'):
    Subscription.objects.filter(user=user).update(
      subscription_type= type,
      subscription_end_time = datetime.now() + timedelta(days=365)

    )

  elif(type == 'Gold'):
    end_date = None
    Subscription.objects.filter(user=user).update(
      subscription_type= type,
      subscription_end_time = end_date

    )

  
  # Keep track on changing customer subscription
  UpdateSubscriptionTrack.objects.create(
    user = user,
    previous_subscription_type = privious_subscription_plan.subscription_type,
    new_subscription_type = type

  )
  
  return Response("Update successfull!")






#Stripe payment gateway
class MakePaymentSession(View):
  def post(self,request, *args, **kwargs):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {          
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.SITE_URL + '?success=true',
            cancel_url=settings.SITE_URL + '?canceled=true',
        )
    except Exception as e:
        return Response(str(e))

    
    







