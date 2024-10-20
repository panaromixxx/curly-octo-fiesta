from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatars = models.ImageField(upload_to='images/avatars/', blank=True)