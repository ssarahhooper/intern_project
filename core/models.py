from django.db import models


# Create your models here.
class Kit(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
