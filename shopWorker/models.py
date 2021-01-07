from django.db import models

# Create your models here.

class ShopWorker(models.Model):
    name=models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    fcm_token = models.CharField(max_length=30)