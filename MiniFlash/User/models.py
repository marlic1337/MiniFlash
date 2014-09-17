from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    about = models.CharField(max_length=32)