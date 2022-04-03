from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.views import APIView
import jwt
from datetime import datetime, timedelta

from django.conf import settings

class Usuario(AbstractUser):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=50, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    # @property
    # def token(self):
    #     token=jwt.encode({'username':self.username, 'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=2)}, settings.SECRET_KEY, algorithm='HS256')
    #     return token