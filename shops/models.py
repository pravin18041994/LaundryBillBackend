from django.db import models

# Create your models here.
from django.db import models


class Shops(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    fcm_token = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    verification_otp = models.CharField(max_length=30, default="")

