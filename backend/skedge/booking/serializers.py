from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['username', 'first_name', 'last_name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['phone_number']


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
        user.last_login = timezone.now()
        user.save()

        Customer.objects.create(user=user, **customer_data)
        return user

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['business_name', 'short_description']


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
        user.last_login = timezone.now()
        user.save()

        Business.objects.create(user=user, **business_data)
        return user


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration']


class FavoriteBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'business_name', 'short_description']


class CustomerBriefSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Customer
        fields = ['phone_number', 'user']

class BusinessBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'business_name', 'short_description']

class CustomerAppointmentSerializer(serializers.ModelSerializer):
    business = BusinessBriefSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ['start_time', 'end_time', 'duration', 'cancelled', 'cancelled_by_customer', 'cancelled_by_business', 'business']

class BusinessAppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerBriefSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ['start_time', 'end_time', 'duration', 'cancelled', 'cancelled_by_customer', 'cancelled_by_business', 'customer']
