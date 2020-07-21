from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    password = models.CharField(max_length=20)
    business_id = models.IntegerField(default=0) # 0 for customer, business_id for employees
    def __str__(self):
        return self.first_name + " " + self.last_name

class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    duration = models.IntegerField()
    business_id = models.IntegerField(default=1) # CHANGE THIS FOR PROD
    last_updated = models.DateTimeField()
    def __str__(self):
        return self.name
