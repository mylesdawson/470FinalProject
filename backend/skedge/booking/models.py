from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# The Django User model is used to store the username, password,
# and email for both customer and business accounts

# Represents a customer account
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=14, default='')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

# Represents a business account
class Business(models.Model):
    FITNESS = 'fitness'
    WELLNESS = 'wellness'
    BEAUTY = 'beauty'
    CATEGORIES = (
        (FITNESS, 'Fitness'),
        (WELLNESS, 'Wellness'),
        (BEAUTY, 'Beauty'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    business_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200) # A short description shown in search results
    long_description = models.CharField(max_length=3000) # A longer description shown on the business page, supports markdown
    contact_email = models.CharField(max_length=50) # Email for customers to contact, can be different from the email used to login
    phone_number = models.CharField(max_length=14) # Phone number for customers to call
    category = models.CharField(max_length=50, choices=CATEGORIES) # Business type

    address = models.CharField(max_length=200) # The business address, excluding city, state, and country
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100) # State or province
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=100)

    # monday_opening_time = models.TimeField()
    # monday_closing_time = models.TimeField()
    # tuesday_opening_time = models.TimeField()
    # tuesday_closing_time = models.TimeField()
    # wednesday_opening_time = models.TimeField()
    # wednesday_closing_time = models.TimeField()
    # thursday_opening_time = models.TimeField()
    # thursday_closing_time = models.TimeField()
    # friday_opening_time = models.TimeField()
    # friday_closing_time = models.TimeField()
    # saturday_opening_time = models.TimeField()
    # saturday_closing_time = models.TimeField()
    # sunday_opening_time = models.TimeField()
    # sunday_closing_time = models.TimeField()

    # days_bookable_in_advance = models.PositiveIntegerField()

    # multiple_employees = models.BooleanField() # Whether the business has multiple employees with different schedules
    # exclusive_customers = models.BooleanField() # Whether the business only allows appointments from whitelisted customers (clients)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

# Represents a specific type of appointment offered by a business
class Service(models.Model):
    DURATIONS = [
        (15, 'Quarter hour'),
        (30, 'Half hour'),
        (45, 'Three quarters hour'),
        (60, 'One hour'),
        (90, 'One and a half hours'),
        (120, 'Two hours'),
        (150, 'Two and a half hours'),
        (180, 'Three hours'),
    ]

    name = models.CharField(max_length=100) # Name of the service
    description = models.CharField(max_length=200) # A short description
    price = models.DecimalField(max_digits=8, decimal_places=2) # Cost to customer
    duration = models.IntegerField(choices=DURATIONS) # Duration in minutes

    #updated_at = models.DateTimeField(auto_now=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    #business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    cancelled = models.BooleanField(default=False)
    cancelled_by_customer = models.BooleanField(default=False)
    cancelled_by_business = models.BooleanField(default=False)

    # A customer has an appointment for a service at a business
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

# Represents a favorited relationship between a customer and a business
# A customer has zero or more favorited businesses
class Favorite(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
