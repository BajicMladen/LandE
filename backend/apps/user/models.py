from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField('Email address', unique=True)
    firebase_uid = models.CharField(max_length=128)
    display_name = models.CharField(max_length=40, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

