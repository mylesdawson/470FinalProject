import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    notes = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + " " + self.last_name
