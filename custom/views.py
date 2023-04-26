from django.shortcuts import render,HttpResponse
# set new custom user
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
def index1(request):
   userobj= User.objects.all()
   print(userobj)
   return HttpResponse('jhbhjb')
