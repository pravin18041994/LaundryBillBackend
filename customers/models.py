from django.db import models
from django.db import models


# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    fcm_token = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, default="")
    payment_type = models.CharField(max_length=30, default="")
    verification_otp = models.CharField(max_length=30, default="")
