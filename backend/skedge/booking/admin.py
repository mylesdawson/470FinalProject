from django.contrib import admin

from .models import Customer, Business, Service, Appointment, Favorite

admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Favorite)
