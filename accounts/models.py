# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):


# class FriendShip(models.Model):


from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models

from .models import User

admin.site.register(User)


class User(AbstractUser):
    email = models.EmailField()
