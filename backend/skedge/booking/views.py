from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, authenticate, get_user_model
from django.contrib.auth.models import User
from django.db.models import Min
from rest_framework import viewsets, status, generics, exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *
import datetime
from calendar import monthrange

from django.views.decorators.csrf import csrf_exempt

# Helper function to get open status, opening hour, closing hour
# each day of the week for a business
def get_business_hours(business):
    days_open = [business.monday_open, business.tuesday_open, business.wednesday_open, business.thursday_open, business.friday_open, business.saturday_open, business.sunday_open]

    opening_times = [business.monday_opening_time, business.tuesday_opening_time, business.wednesday_opening_time, business.thursday_opening_time, business.friday_opening_time, business.saturday_opening_time, business.sunday_opening_time]

    closing_times = [business.monday_closing_time, business.tuesday_closing_time, business.wednesday_closing_time, business.thursday_closing_time, business.friday_closing_time, business.saturday_closing_time, business.sunday_closing_time]

    return days_open, opening_times, closing_times

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

class Login(ObtainAuthToken):
    permission_classes = []

    def post(self, request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print(username)
        print(password)

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        print(user.pk)

        account_type = 'customer'
        customer = Customer.objects.filter(user=user)
        business = None
        if customer is None:
            business = Business.objects.filter(user=user)
            account_type = 'business'
            if business is None:
                raise exceptions.AuthenticationFailed(_('Somehow this User has no attached Customer or Business account'))
            else:
                business = business[0]
        else:
            customer = customer[0]

        print(customer)
        print(business)

        token, created = Token.objects.get_or_create(user=user)
        print(token)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'account_type': account_type,
            'account_id': customer.pk if customer else business.pk
        })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerUserSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BusinessUserSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

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

# Return all services of a specific business
def business_services(request, business_id):
    if request.method == 'GET':
        services = Service.objects.filter(business=business_id)
        serializer = ServiceSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

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
        appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__month=month, date__day=day)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

def business_appointments_by_week(request, business_id, year, week):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__week=week)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})


def business_appointments_by_month(request, business_id, year, month):
    if request.method == 'GET':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotExist:
            return JsonResponse({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

        days_open, opening_times, closing_times = get_business_hours(business)

        try:
            min_duration = Service.objects.filter(business=business_id).aggregate(Min('duration'))['duration__min']
        except AttributeError:
            return JsonResponse({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

        _, days_in_month = monthrange(year, month)

        appointments = Appointment.objects.filter(business=business_id, date__year=year, date__month=month, cancelled=False)
        data = {}


        for day in range(1, days_in_month+1):
            day_of_week = datetime.datetime(year, month, day).weekday()

            if days_open[day_of_week] == True:
                # day_appointments = list(appointments.filter(date__day=day).values('start_time', 'end_time').order_by('start_time'))
                day_appointments.insert(0, {'end_time': opening_times[day_of_week]})
                day_appointments.append({'start_time': closing_times[day_of_week]})
                print(day_appointments)
                fully_booked = True
                for i in range(1, len(day_appointments)):
                    date = datetime.date(1, 1, 1)
                    first_time = datetime.datetime.combine(date, day_appointments[i-1]['end_time'])
                    second_time = datetime.datetime.combine(date, day_appointments[i]['start_time'])
                    interval = second_time - first_time

                    if (interval.total_seconds() // 60) >= min_duration:
                        fully_booked = False
                        break

                if fully_booked == True:
                    availibility = 'booked'
                else:
                    availibility = 'open'
            else:
                availibility = 'closed'
            data[day] = availibility

        return JsonResponse(data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

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


def services_available_times(request, business_id, year, month, day):
    if request.method == 'GET':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotExist:
            return JsonResponse({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

        day_of_week = datetime.datetime(year, month, day).weekday()
        days_open, opening_times, closing_times = get_business_hours(business)

        if days_open[day_of_week] == False:
            return JsonResponse([], safe=False)

        services = Service.objects.filter(business=business_id)
        # appointments = list(Appointment.objects.filter(business=business_id, date__year=year, date__month=month, date__day=day).values('start_time', 'end_time').order_by('start_time'))
        appointments.insert(0, {'end_time': opening_times[day_of_week]})
        appointments.append({'start_time': closing_times[day_of_week]})

        data = []

        for service in services:
            serializer = ServiceSerializer(service, many=False)
            service_data = serializer.data
            times = []

            for i in range(1, len(appointments)):
                date = datetime.date(1, 1, 1)
                first_time = datetime.datetime.combine(date, appointments[i-1]['end_time'])
                second_time = datetime.datetime.combine(date, appointments[i]['start_time'])
                interval = second_time - first_time

                while (interval.total_seconds() // 60) >= service.duration:
                    times.append('{:d}:{:02d}'.format(first_time.hour, first_time.minute))
                    first_time = first_time + datetime.timedelta(seconds=60*MIN_DURATION)
                    interval = second_time - first_time

            service_data['times'] = times
            data.append(service_data)

        return JsonResponse(data, safe=False)



    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

@csrf_exempt
def business_cancel_appointment(request, business_id, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(pk=appointment_id, business=business_id)
        except Business.DoesNotExist:
            return JsonResponse({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

        appointment.cancelled = True
        appointment.cancelled_by_business = True
        appointment.cancelled_by_customer = False
        appointment.save()

        serializer = BusinessAppointmentSerializer(appointment, many=False)

        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})

@csrf_exempt
def customer_cancel_appointment(request, customer_id, appointment_id):
    return JsonResponse(status=400, data={'status':'false', 'message':'Bad request'})
