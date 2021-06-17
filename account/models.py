from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    job = models.CharField(max_length=50)
    major = models.CharField(max_length=30)
    level = models.CharField(max_length=10)
    age = models.CharField(max_length=10)