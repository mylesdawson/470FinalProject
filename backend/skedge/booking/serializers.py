from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
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
        fields = ['id', 'business_name', 'short_description', 'long_description', 'contact_email', 'phone_number', 'category', 'address', 'city', 'province', 'postal_code', 'monday_open', 'tuesday_open', 'wednesday_open', 'thursday_open', 'friday_open', 'saturday_open', 'sunday_open', 'monday_opening_time', 'tuesday_opening_time', 'wednesday_opening_time', 'thursday_opening_time', 'friday_opening_time', 'saturday_opening_time', 'sunday_opening_time', 'monday_closing_time', 'tuesday_closing_time', 'wednesday_closing_time', 'thursday_closing_time', 'friday_closing_time', 'saturday_closing_time', 'sunday_closing_time', 'days_bookable_in_advance', 'hours_notice_in_advance']


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
        fields = ['id', 'name', 'description', 'price', 'duration', 'deleted', 'business']

    def create(self, validated_data):
        business = validated_data.pop('business')
        service = Service.objects.create(business=business, **validated_data)
        return service

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'date', 'start_time', 'end_time', 'customer', 'business', 'service']

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        service = validated_data.pop('service')
        business = validated_data.pop('business')

        appointment = Appointment.objects.create(customer=customer, service=service, business=business, **validated_data)
        return appointment


class CustomerBriefSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Customer
        fields = ['phone_number', 'user']

class BusinessBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'business_name', 'short_description']

class ServiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'deleted', 'duration']

class CustomerAppointmentSerializer(serializers.ModelSerializer):
    business = BusinessBriefSerializer(many=False, read_only=True)
    service = ServiceBriefSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'start_time', 'end_time', 'cancelled', 'cancelled_by_customer', 'cancelled_by_business', 'business', 'service']

class BusinessAppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerBriefSerializer(many=False, read_only=True)
    service = ServiceBriefSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'start_time', 'end_time', 'cancelled', 'cancelled_by_customer', 'cancelled_by_business', 'customer', 'service']
