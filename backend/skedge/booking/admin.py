from django.contrib import admin

from .models import Customer, Business, Service, Appointment, Favorites, Employee, Client

admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Favorites)
admin.site.register(Employee)
admin.site.register(Client)
