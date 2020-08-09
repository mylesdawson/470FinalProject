from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

DURATIONS = [
    (15, '15'),
    (30, '30'),
    (45, '45'),
    (60, '1:00'),
    (90, '1:30'),
    (120, '2:00'),
    (150, '2:30'),
    (180, '3:00'),
]
MIN_DURATION = min([d[0] for d in DURATIONS])

ALL = 'all'
FITNESS = 'fitness'
WELLNESS = 'wellness'
BEAUTY = 'beauty'
MISCELLANEOUS = 'miscellaneous'
CATEGORIES = [
    (ALL, 'All'),
    (FITNESS, 'Fitness'),
    (WELLNESS, 'Wellness'),
    (BEAUTY, 'Beauty'),
    (MISCELLANEOUS, 'Miscellaneous')
]


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    business_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200, blank=True) # A short description shown in search results
    long_description = models.CharField(max_length=3000, blank=True) # A longer description shown on the business page, supports markdown
    contact_email = models.CharField(max_length=50, blank=True) # Email for customers to contact, can be different from the email used to login
    phone_number = models.CharField(max_length=14, blank=True) # Phone number for customers to call
    category = models.CharField(max_length=50, choices=CATEGORIES, default=WELLNESS) # Business type

    address = models.CharField(max_length=200, blank=True) # The business address, excluding city, state, and country
    city = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True) # State or province
    postal_code = models.CharField(max_length=6, blank=True)

    monday_open = models.BooleanField(default=True)
    tuesday_open = models.BooleanField(default=True)
    wednesday_open = models.BooleanField(default=True)
    thursday_open = models.BooleanField(default=True)
    friday_open = models.BooleanField(default=True)
    saturday_open = models.BooleanField(default=False)
    sunday_open = models.BooleanField(default=False)

    monday_opening_time = models.TimeField(default='9:00')
    tuesday_opening_time = models.TimeField(default='9:00')
    wednesday_opening_time = models.TimeField(default='9:00')
    thursday_opening_time = models.TimeField(default='9:00')
    friday_opening_time = models.TimeField(default='9:00')
    saturday_opening_time = models.TimeField(default='9:00')
    sunday_opening_time = models.TimeField(default='9:00')

    monday_closing_time = models.TimeField(default='17:00')
    tuesday_closing_time = models.TimeField(default='17:00')
    wednesday_closing_time = models.TimeField(default='17:00')
    thursday_closing_time = models.TimeField(default='17:00')
    friday_closing_time = models.TimeField(default='17:00')
    saturday_closing_time = models.TimeField(default='17:00')
    sunday_closing_time = models.TimeField(default='17:00')

    days_bookable_in_advance = models.PositiveIntegerField(default=14)
    hours_notice_in_advance = models.PositiveIntegerField(default=1)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

# Represents a specific type of appointment offered by a business
class Service(models.Model):

    name = models.CharField(max_length=100) # Name of the service
    description = models.CharField(max_length=200) # A short description
    price = models.DecimalField(max_digits=8, decimal_places=2) # Cost to customer
    duration = models.IntegerField(choices=DURATIONS) # Duration in minutes

    deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

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
