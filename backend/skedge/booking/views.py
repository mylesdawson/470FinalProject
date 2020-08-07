from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *
import datetime

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # get request username/password
        print(request)
        print(request.user)
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerUserSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BusinessUserSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Parse phone number into standard format
def parse_phone_number(phone_number):
    if phone_number != '':
        phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
        phone_number = '{}-{}-{}'.format(phone_number[0:3], phone_number[3:6], phone_number[6:10])
    return phone_number

def new_customer(request):
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = parse_phone_number(request.POST['phone_number'])

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.save()
    customer = Customer(
        user=user,
        phone_number=phone_number
    )
    customer.save()

    return

def edit_customer(request, user_id):
    user = User.objects.get(pk=user_id)
    customer = user.customer

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = parse_phone_number(request.POST['phone_number'])

        user.username = username
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        customer.phone_number = phone_number

        user.save()
        customer.save()

        # Rerender page with changes
    else:
        # Render edit page
        return

    return

def new_business(request, user_id):
    user = User.objects.get(pk=user_id)

    username = method.POST['username']
    password = method.POST['password']
    email = method.POST['email']
    first_name = method.POST['first_name']
    last_name = method.POST['last_name']

    business_name = method.POST['name']
    short_description = method.POST['short_description']
    long_description = method.POST['long_description']
    address = method.POST['address']
    city = method.POST['city']
    state = method.POST['state']
    postal_code = method.POST['postal_code']
    country = method.POST['country']
    contact_email = method.POST['contact_email']
    phone_number = method.POST['phone_number']
    category = method.POST['category']
    multiple_employees = method.POST['multiple_employees']
    exclusive_customers = method.POST['exclusive_customers']

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.save()
    business = Business(
        business_name=business_name,
        short_description=short_description,
        long_description=long_description,
        address=address,
        city=city,
        state=state,
        postal_code=postal_code,
        country=country,
        contact_email=contact_email,
        phone_number=phone_number,
        category=category,
        multiple_employees=multiple_employees,
        exclusive_customers=exclusive_customers,
    )

    user.save()
    business.save()

    # Render home page
    return

def edit_business(request):
    user = User.objects.get(pk=user_id)
    business = user.business

    username = method.POST['username']
    password = method.POST['password']
    email = method.POST['email']
    first_name = method.POST['first_name']
    last_name = method.POST['last_name']

    business_name = method.POST['name']
    short_description = method.POST['short_description']
    long_description = method.POST['long_description']
    address = method.POST['address']
    city = method.POST['city']
    state = method.POST['state']
    postal_code = method.POST['postal_code']
    country = method.POST['country']
    contact_email = method.POST['contact_email']
    phone_number = method.POST['phone_number']
    category = method.POST['category']
    multiple_employees = method.POST['multiple_employees']
    exclusive_customers = method.POST['exclusive_customers']

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.save()
    business = Business(
        business_name=business_name,
        short_description=short_description,
        long_description=long_description,
        address=address,
        city=city,
        state=state,
        postal_code=postal_code,
        country=country,
        contact_email=contact_email,
        phone_number=phone_number,
        category=category,
        multiple_employees=multiple_employees,
        exclusive_customers=exclusive_customers,
    )

    user.save()
    business.save()

    # Render home page
    return

# Return all of a customer's favorited businesses
def favorite_businesses(request, customer_id):
    if request.method == 'GET':
        businesses = Business.objects.filter(favorite__customer=customer_id)
        serializer = FavoriteBusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

def customer_appointments(request, customer_id):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('business', 'service').filter(customer=customer_id)
        serializer = CustomerAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})


def business_appointments_by_day(request, business_id, year, month, day):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('customer').filter(business=business_id, date__year=year, date__month=month, date__day=day)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

def business_appointments_by_week(request, business_id, year, week):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('customer').filter(business=business_id, date__year=year, date__week=week)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

# def search_businesses(request, search):
#     if request.method == 'GET':
#         businesses = Business.objects.filter()

def businesses_by_category(request, category):
    if request.method == 'GET' and category in dict(CATEGORIES):
        if category == ALL:
            businesses = Business.objects.all()
        else:
            businesses = Business.objects.filter(category=category)

        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

def businesses_search(request, category, search):
    if request.method == 'GET' and category in dict(CATEGORIES):
        if category == ALL:
            businesses = Business.objects.filter(business_name__startswith=search)
        else:
            businesses = Business.objects.filter(category=category, business_name__startswith=search)

        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})
