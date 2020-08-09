from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, authenticate, get_user_model
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.db.models import Min
from rest_framework import viewsets, status, generics, exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from .serializers import *
import datetime
import pytz
from calendar import monthrange
from django.views.decorators.csrf import csrf_exempt

timezone = pytz.timezone('America/Vancouver')

###############################################################
# Helper functions
###############################################################

# Helper function to get open status, opening hour, closing hour
# each day of the week for a business
def get_business_hours(business):
    days_open = [business.monday_open, business.tuesday_open, business.wednesday_open, business.thursday_open, business.friday_open, business.saturday_open, business.sunday_open]

    opening_times = [business.monday_opening_time, business.tuesday_opening_time, business.wednesday_opening_time, business.thursday_opening_time, business.friday_opening_time, business.saturday_opening_time, business.sunday_opening_time]

    closing_times = [business.monday_closing_time, business.tuesday_closing_time, business.wednesday_closing_time, business.thursday_closing_time, business.friday_closing_time, business.saturday_closing_time, business.sunday_closing_time]

    return days_open, opening_times, closing_times

# Parse phone number into standard format
def parse_phone_number(phone_number):
    if phone_number != '':
        phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
        phone_number = '{}-{}-{}'.format(phone_number[0:3], phone_number[3:6], phone_number[6:10])
    return phone_number

###############################################################
# Authentication
###############################################################

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'token': token})

def authenticate_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id, user=request.user.id)
    except Customer.DoesNotExist:
        raise AuthenticationFailed

    return customer

def authenticate_business(request, business_id):
    try:
        business = Business.objects.get(id=business_id, user=request.user.id)
    except Business.DoesNotExist:
        raise AuthenticationFailed

    return business

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
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        print(user.pk)

        account_type = 'customer'
        customer = Customer.objects.filter(user=user)
        business = None
        if customer is None:
            business = Business.objects.filter(user=user)
            account_type = 'business'
            if business is None:
                raise exceptions.AuthenticationFailed('Somehow this User has no attached Customer or Business account')
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

# Returns the information about a business
def business_info(request, business_id):
    if request.method == 'GET':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        serializer = BusinessSerializer(business, many=False)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Edits the main information of a business
@api_view(['POST'])
@csrf_exempt
def edit_main_business_info(request, business_id):
    if request.method == 'POST':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotException:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        try:
            business.business_name = request.POST['business_name']
            business.short_description = request.POST['short_description']
            business.long_description = request.POST['long_description']
            business.contact_email = request.POST['contact_email']
            business.phone_number = parse_phone_number(request.POST['phone_number'])
            business.category = request.POST['category']

            business.full_clean()
            business.save()

            serializer = BusinessSerializer(business, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

def edit_location_business_info(request, business_id):
    if request.method == 'POST':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotException:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        try:
            business.address = request.POST['address']
            business.city = request.POST['city']
            business.province = request.POST['province']
            business.postal_code = request.POST['postal_code']

            business.full_clean()
            business.save()

            serializer = BusinessSerializer(business, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

def edit_hours_business_info(request, business_id):
    if request.method == 'POST':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotException:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        try:
            business.monday_open = request.POST['monday_open']
            business.tuesday_open = request.POST['tuesday_open']
            business.wednesday_open = request.POST['wednesday_open']
            business.thursday_open = request.POST['thursday_open']
            business.friday_open = request.POST['friday_open']
            business.saturday_open = request.POST['saturday_open']
            business.sunday_open = request.POST['sunday_open']

            business.monday_opening_time = request.POST['monday_opening_time']
            business.tuesday_opening_time = request.POST['tuesday_opening_time']
            business.wednesday_opening_time = request.POST['wednesday_opening_time']
            business.thursday_opening_time = request.POST['thursday_opening_time']
            business.friday_opening_time = request.POST['friday_opening_time']
            business.saturday_opening_time = request.POST['saturday_opening_time']
            business.sunday_opening_time = request.POST['sunday_opening_time']

            business.monday_closing_time = request.POST['monday_closing_time']
            business.tuesday_closing_time = request.POST['tuesday_closing_time']
            business.wednesday_closing_time = request.POST['wednesday_closing_time']
            business.thursday_closing_time = request.POST['thursday_closing_time']
            business.friday_closing_time = request.POST['friday_closing_time']
            business.saturday_closing_time = request.POST['saturday_closing_time']
            business.sunday_closing_time = request.POST['sunday_closing_time']

            business.full_clean()
            business.save()

            serializer = BusinessSerializer(business, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Return all services of a specific business
def business_services(request, business_id):
    print(request.user)
    if request.method == 'GET':
        services = Service.objects.filter(business=business_id)
        serializer = ServiceSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

###############################################################
# Favorites
###############################################################

# Return all of a customer's favorited businesses
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def favorite_businesses(request, customer_id):
    authenticate_customer(request, customer_id)

    if request.method == 'GET':
        businesses = Business.objects.filter(favorite__customer=customer_id)
        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Add a business to a customer's favorited businesses
def add_favorite_business(request, customer_id, business_id):

    return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

# Remove a business from a customer's favorited businesses
def remove_favorite_business(request, customer_id, business_id):

    return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

###############################################################
# Favorites
###############################################################

# Returns all of a customer's appointments
def customer_appointments(request, customer_id):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('business', 'service').filter(customer=customer_id)
        serializer = CustomerAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Returns all of a business's appointments for a specific day
def business_appointments_by_day(request, business_id, year, month, day):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__month=month, date__day=day)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Returns all of a business's appointments for a specific month
def business_appointments_by_week(request, business_id, year, week):
    if request.method == 'GET':
        appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__week=week)
        serializer = BusinessAppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

###############################################################
# Services
###############################################################

# Returns the available appointment time slots for each service of a business for a specific day
def services_available_times(request, business_id, year, month, day):
    if request.method == 'GET':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        date = datetime.date(year, month, day)
        day_of_week = date.weekday()
        days_open, opening_times, closing_times = get_business_hours(business)
        current_date = datetime.datetime.now(tz=timezone).date()
        days_between = (date - current_date).days
        earliest_bookable_time = datetime.datetime.combine(datetime.date(1, 1, 1), datetime.datetime.now(tz=timezone).time())
        earliest_bookable_time += datetime.timedelta(hours=business.hours_notice_in_advance)

        if days_between < 0:
            availability = 'past'
        elif days_between > business.days_bookable_in_advance:
            availability = 'unavailable'
        elif days_open[day_of_week] == False:
            availability = 'closed'
        else:
            availability = 'open'

        if availability != 'open':
            return JsonResponse({'availability': availability, 'services': []}, safe=False)

        services = Service.objects.filter(business=business_id)
        appointments = list(Appointment.objects.filter(business=business_id, date__year=year, date__month=month, date__day=day).values('start_time', 'end_time').order_by('start_time'))
        appointments.insert(0, {'end_time': opening_times[day_of_week]})
        appointments.append({'start_time': closing_times[day_of_week]})

        data = {'availability': 'open', 'services': []}

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
                    if days_between > 0 or first_time >= earliest_bookable_time:
                        times.append('{:d}:{:02d}'.format(first_time.hour, first_time.minute))
                    first_time = first_time + datetime.timedelta(seconds=60*MIN_DURATION)
                    interval = second_time - first_time

            service_data['times'] = times
            data['services'].append(service_data)

        return JsonResponse(data, safe=False)



    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

def services_available_days(request, business_id, year, month):
    if request.method == 'GET':
        try:
            business = Business.objects.get(pk=business_id)
        except Business.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        days_open, opening_times, closing_times = get_business_hours(business)

        try:
            min_duration = Service.objects.filter(business=business_id).aggregate(Min('duration'))['duration__min']
        except AttributeError:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        _, days_in_month = monthrange(year, month)

        appointments = Appointment.objects.filter(business=business_id, date__year=year, date__month=month, cancelled=False)
        data = {}
        current_date = datetime.datetime.now(tz=timezone).date()

        for day in range(1, days_in_month+1):
            date = datetime.date(year, month, day)
            day_of_week = date.weekday()
            days_between = (date - current_date).days

            if days_between < 0:
                availability = 'past'
            elif days_between > business.days_bookable_in_advance:
                availability = 'unavailable'
            elif days_open[day_of_week] == True:
                day_appointments = list(appointments.filter(date__day=day).values('start_time', 'end_time').order_by('start_time'))
                day_appointments.insert(0, {'end_time': opening_times[day_of_week]})
                day_appointments.append({'start_time': closing_times[day_of_week]})

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
                    availability = 'booked'
                else:
                    availability = 'open'
            else:
                availability = 'closed'
            data[day] = availability

        return JsonResponse(data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

###############################################################
# Search
###############################################################

def businesses_by_category(request, category):
    if request.method == 'GET' and category in dict(CATEGORIES):
        if category == ALL:
            businesses = Business.objects.all()
        else:
            businesses = Business.objects.filter(category=category)

        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

def businesses_search(request, category, search):
    if request.method == 'GET' and category in dict(CATEGORIES):
        if category == ALL:
            businesses = Business.objects.filter(business_name__startswith=search)
        else:
            businesses = Business.objects.filter(category=category, business_name__startswith=search)

        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

###############################################################
# Appointments
###############################################################

@csrf_exempt # Remove when authentication is working
def business_cancel_appointment(request, business_id, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(pk=appointment_id, business=business_id)
        except Appointment.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        if appointment.cancelled:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

        appointment.cancelled = True
        appointment.cancelled_by_business = True
        appointment.cancelled_by_customer = False
        appointment.save()

        serializer = BusinessAppointmentSerializer(appointment, many=False)

        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# @csrf_exempt # Remove when authentication is working
@api_view(['POST'])
def customer_cancel_appointment(request, customer_id, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(pk=appointment_id, customer=customer_id)
        except Appointment.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

        if appointment.cancelled:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

        appointment.cancelled = True
        appointment.cancelled_by_customer = True
        appointment.cancelled_by_business = False
        appointment.save()

        serializer = CustomerAppointmentSerializer(appointment, many=False)

        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})
