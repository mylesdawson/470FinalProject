from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Business, Employee, Service, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'customer']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        customer_data = validated_data.pop('customer')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        Customer.objects.create(user=user, **customer_data)
        return user



class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'business']

    def create(self, validated_data):
        password = validated_data.pop('password')
        business_data = validated_data.pop('business')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        Business.objects.create(user=user, **business_data)
        return user


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration', 'business_id', 'last_updated']
