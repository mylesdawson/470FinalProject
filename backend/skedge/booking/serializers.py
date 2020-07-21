from rest_framework import serializers
from .models import User, Business, Service

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['name', 'description', 'email', 'phone_number']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration', 'business_id', 'last_updated']
