from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserInfo
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
    phoneNumber = request.POST.get('phoneNumber')

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


  


