from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from helpers.models import TrackingModel


class User(TrackingModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    meta_data = models.JSONField(
        default=dict, null=True, blank=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
