from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Business, Employee, Service, Appointment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # TODO: fill in required Customer fields if needed
        # For now lets only require a user to enter a username and password
        fields = []


class CustomerUserSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'customer']
        # TODO: add this back when in production and add to business as well
        # extra_kwargs = {'password': {'write_only': True}}

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
        model = Business
        fields = ['business_name', 'short_description', ]


class BusinessUserSerializer(serializers.HyperlinkedModelSerializer):
    business = BusinessSerializer(required=True)

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
