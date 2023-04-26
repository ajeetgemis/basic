from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import managers
class customuser(AbstractUser):
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    username=None
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=managers()
