from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserInfo
from random import randint
from .serializers import userSeriliazer
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

    

    # validate phone number start -------->>>>>>

    range_start = 10**(8-1)   
    range_end = (10**8)-1
    rand_number = randint(range_start, range_end)  #random last 8 digit number
    rand_number = str(rand_number)
    country_code = '+88'
    phn_operator_code = ['017','016','019','015','018']
    rand_operator_code = phn_operator_code[randint(0,4)] 
    phoneNumber = country_code + rand_operator_code + rand_number
    #print('Phone number ...',phoneNumber)

   #  validate phone number end ------>>>>>>>>>>




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



@api_view(['GET'])
def getUnsubcribedUserPhoneNumber(request):

  unsubcribed_user_info = UserInfo.objects.filter(subscription__subscription_type__contains= '')

  user_serializer= userSeriliazer(unsubcribed_user_info, many=True)

  return Response(user_serializer.data)




