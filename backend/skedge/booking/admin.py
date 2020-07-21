from django.contrib import admin

from .models import User, Business, Service

# Register your models here.
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Service)