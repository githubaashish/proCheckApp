from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetailsInfo(models.Model):

    # user parameters
    user = models.OneToOneField(User)   # One to One mapping from User class
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
