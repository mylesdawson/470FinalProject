from django.conf import settings
from django.db import models

# Use User model to store only username and password
# for both customer and business accounts

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    last_updated = models.DateTimeField()
    created = models.DateTimeField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Business(models.Model):
    CATEGORIES = (
        ('fitness', 'Fitness'),
        ('wellness', 'Wellness'),
        ('beauty', 'Beauty'),
    )

    name = models.CharField(max_length=50) # Business name
    short_description = models.CharField(max_length=200) # A short description shown in search results
    long_description = models.CharField(max_length=3000) # A longer description shown on the business page, supports markdown
    address = models.CharField(max_length=200) # The business address, excluding city, state, and country
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100) # State or province
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=50) # Email for customers to contact, can be different from the email used to login
    phone_number = models.CharField(max_length=14) # Phone number for customers to call
    category = models.CharField(max_length=50, choices=CATEGORIES) # Business type
    multiple_employees = models.BooleanField() # Whether the business has multiple employees with different schedules
    exclusive_customers = models.BooleanField() # Whether the business only allows appointments from whitelisted customers (clients)
    last_updated = models.DateTimeField()
    created = models.DateTimeField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Service(models.Model):
    name = models.CharField(max_length=50) # Name of the service
    description = models.CharField(max_length=200) # A short description
    price = models.DecimalField(max_digits=8, decimal_places=2) # Cost to customer
    duration = models.IntegerField() # Duration in minutes
    last_updated = models.DateTimeField()
    created = models.DateTimeField()

    models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # A customer has an appointment for a service at a business
    models.ForeignKey(Customer, on_delete=models.CASCADE)
    models.ForeignKey(Service, on_delete=models.CASCADE)
    models.ForeignKey(Business, on_delete=models.CASCADE)

# A client is a customer that has been whitelisted for a specific business
class Client(models.Model):
    created = models.DateTimeField()

    models.ForeignKey(Customer, on_delete=models.CASCADE)
    models.ForeignKey(Business, on_delete=models.CASCADE)
