from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField("users/%Y/%m/%d/", blank=True, null=True)

