from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, authenticate, get_user_model
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.db.models import Min
from django.utils import dateparse
from rest_framework import viewsets, status, generics, exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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

        try:
            customer = Customer.objects.get(user=user)
            account_type = 'customer'
            account_id = customer.pk
        except Customer.DoesNotExist:
            try:
                business = Business.objects.get(user=user)
                account_type = 'business'
                account_id = business.pk
            except Business.DoesNotExist:
                raise AuthenticationFailed('User has no attached Customer or Business account')

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'account_type': account_type,
            'account_id': account_id
        })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BusinessUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]



def new_customer(request):
    username = request.data['username']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    phone_number = parse_phone_number(request.data['phone_number'])

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
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone_number = parse_phone_number(request.data['phone_number'])

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

###############################################################
# Businesses
###############################################################

# Returns the information about a business
@api_view(['GET'])
def business_info(request, business_id):
    try:
        business = Business.objects.get(pk=business_id)
    except Business.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    serializer = BusinessSerializer(business, many=False)
    return JsonResponse(serializer.data, safe=False)

# Edits the account information of a business
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_business_account(request, business_id):
    business = authenticate_business(request, business_id)

    try:
        user = business.user
        user.username = request.data['username']
        user.set_password(request.data['password'])
        user.save()
    except Exception:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Edits the main information of a business
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_main_business_info(request, business_id):
    business = authenticate_business(request, business_id)

    try:
        business.business_name = request.data['business_name']
        business.short_description = request.data['short_description']
        business.long_description = request.data['long_description']
        business.contact_email = request.data['contact_email']
        business.phone_number = parse_phone_number(request.data['phone_number'])
        business.category = request.data['category']

        business.full_clean()
        business.save()

        serializer = BusinessSerializer(business, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Edits the location information of a business
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_location_business_info(request, business_id):
    business = authenticate_business(request, business_id)

    try:
        business.address = request.data['address']
        business.city = request.data['city']
        business.province = request.data['province']
        business.postal_code = request.data['postal_code']

        business.full_clean()
        business.save()

        serializer = BusinessSerializer(business, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Edits the hours information of a business
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_hours_business_info(request, business_id):
    business = authenticate_business(request, business_id)

    try:
        business.monday_open = request.data['monday_open']
        business.tuesday_open = request.data['tuesday_open']
        business.wednesday_open = request.data['wednesday_open']
        business.thursday_open = request.data['thursday_open']
        business.friday_open = request.data['friday_open']
        business.saturday_open = request.data['saturday_open']
        business.sunday_open = request.data['sunday_open']

        business.monday_opening_time = request.data['monday_opening_time']
        business.tuesday_opening_time = request.data['tuesday_opening_time']
        business.wednesday_opening_time = request.data['wednesday_opening_time']
        business.thursday_opening_time = request.data['thursday_opening_time']
        business.friday_opening_time = request.data['friday_opening_time']
        business.saturday_opening_time = request.data['saturday_opening_time']
        business.sunday_opening_time = request.data['sunday_opening_time']

        business.monday_closing_time = request.data['monday_closing_time']
        business.tuesday_closing_time = request.data['tuesday_closing_time']
        business.wednesday_closing_time = request.data['wednesday_closing_time']
        business.thursday_closing_time = request.data['thursday_closing_time']
        business.friday_closing_time = request.data['friday_closing_time']
        business.saturday_closing_time = request.data['saturday_closing_time']
        business.sunday_closing_time = request.data['sunday_closing_time']

        business.days_bookable_in_advance = request.data['days_bookable_in_advance']
        business.hours_notice_in_advance = request.data['hours_notice_in_advance']

        business.full_clean()
        business.save()

        serializer = BusinessSerializer(business, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

###############################################################
# Favorites
###############################################################

# Return all of a customer's favorited businesses
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def favorite_businesses(request, customer_id):
    authenticate_customer(request, customer_id)

    businesses = Business.objects.filter(favorite__customer=customer_id)
    serializer = BusinessSerializer(businesses, many=True)
    return JsonResponse(serializer.data, safe=False)

# Add a business to a customer's favorited businesses
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_favorite_business(request, customer_id, business_id):
    customer = authenticate_customer(request, customer_id)

    try:
        business = Business.objects.get(pk=business_id)
    except Business.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    try:
        existing_favorite = Favorite.objects.get(customer=customer, business=business)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})
    except Favorite.DoesNotExist:
        favorite = Favorite(
            customer=customer,
            business=business
        )
        favorite.save()

        serializer = FavoriteSerializer(favorite, many=False)
        return JsonResponse(serializer.data, safe=False)


# Remove a business from a customer's favorited businesses
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def remove_favorite_business(request, customer_id, business_id):
    customer = authenticate_customer(request, customer_id)

    try:
        favorite = Favorite.objects.get(customer=customer, business_id=business_id)
        favorite.delete()
        serializer = FavoriteSerializer(favorite, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Favorite.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

###############################################################
# Services
###############################################################

# Return all services of a specific business
@api_view(['GET'])
def business_services(request, business_id):
    services = Service.objects.filter(business=business_id, deleted=False)
    serializer = ServiceSerializer(services, many=True)
    return JsonResponse(serializer.data, safe=False)

# Creates a new service for a business
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def new_business_service(request, business_id):
    business = authenticate_business(request, business_id)

    try:
        service = Service(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price'],
            duration=request.data['duration'],
            business=business
        )
        service.full_clean()
        service.save()

        serializer = ServiceSerializer(service, many=False)
        return JsonResponse(serializer.data, safe=False)

    except Exception:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Deletes a service for a business
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_business_service(request, business_id, service_id):
    authenticate_business(request, business_id)

    try:
        service = Service.objects.get(pk=service_id, deleted=False)
        service.deleted = True
        service.save()

        appointments = Appointment.objects.filter(service_id=service_id)
        appointments.update(cancelled=True, cancelled_by_business=True)
        for appointment in appointments:
            appointment.save()

        serializer = ServiceSerializer(service, many=False)
        return JsonResponse(serializer.data, safe=False)

    except Service.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

# Returns the available appointment time slots for each service of a business for a specific day
@api_view(['GET'])
def services_available_times(request, business_id, year, month, day):
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

    services = Service.objects.filter(business=business_id, deleted=False)
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

@api_view(['GET'])
def services_available_days(request, business_id, year, month):
    try:
        business = Business.objects.get(pk=business_id)
    except Business.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    days_open, opening_times, closing_times = get_business_hours(business)

    try:
        min_duration = Service.objects.filter(business=business_id, deleted=False).aggregate(Min('duration'))['duration__min']
    except AttributeError:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    _, days_in_month = monthrange(year, month)

    appointments = Appointment.objects.filter(business=business_id, date__year=year, date__month=month, cancelled=False)
    data = []
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
        data.append({'date': day, 'status': availability})

    return JsonResponse(data, safe=False)

###############################################################
# Search
###############################################################

# Returns all businesses in the specified category
@api_view(['GET'])
def businesses_by_category(request, category):
    if request.method == 'GET' and category in dict(CATEGORIES):
        if category == ALL:
            businesses = Business.objects.all()
        else:
            businesses = Business.objects.filter(category=category)

        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

# Returns all businesses in the specified category whose name begins with the search term
@api_view(['GET'])
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

# Returns all of a customer's appointments
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def customer_appointments(request, customer_id):
    authenticate_customer(request, customer_id)

    appointments = Appointment.objects.select_related('business', 'service').filter(customer=customer_id)
    serializer = CustomerAppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)


# Returns all of a business's appointments for a specific day
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def business_appointments_by_day(request, business_id, year, month, day):
    authenticate_business(request, business_id)

    appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__month=month, date__day=day)
    serializer = BusinessAppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)


# Returns all of a business's appointments for a specific month
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def business_appointments_by_week(request, business_id, year, week):
    authenticate_business(request, business_id)

    appointments = Appointment.objects.select_related('customer', 'service', 'customer__user').filter(business=business_id, date__year=year, date__week=week)
    serializer = BusinessAppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)


# Returns all of a business's appointments for a specific month
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def business_appointments_by_month(request, business_id, year, month):
    business = authenticate_business(request, business_id)

    days_open, opening_times, closing_times = get_business_hours(business)

    try:
        min_duration = Service.objects.filter(business=business_id, deleted=False).aggregate(Min('duration'))['duration__min']
    except AttributeError:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    _, days_in_month = monthrange(year, month)

    appointments = Appointment.objects.filter(business=business_id, date__year=year, date__month=month, cancelled=False)
    data = []
    current_date = datetime.datetime.now(tz=timezone).date()

    for day in range(1, days_in_month+1):
        date = datetime.date(year, month, day)
        day_of_week = date.weekday()
        days_between = (date - current_date).days

        day_appointments = list(appointments.filter(date__day=day).values('start_time', 'end_time').order_by('start_time'))
        num_appointments = len(day_appointments)

        if days_between < 0:
            availability = 'past'
        elif days_between > business.days_bookable_in_advance:
            availability = 'unavailable'
        elif days_open[day_of_week] == True:

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
        data.append({'date': date, 'status': availability, 'appointments': num_appointments})

    return JsonResponse(data, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def new_customer_appointment(request, customer_id):
    customer = authenticate_customer(request, customer_id)

    try:
        business = Business.objects.get(pk=request.data['business_id'])
        service = Service.objects.get(pk=request.data['service_id'], deleted=False)
    except (Business.DoesNotExist, Service.DoesNotExist):
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'status': 'details'})

    if service.business_id != int(request.data['business_id']):
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid service for business'})

    try:
        appointment = Appointment(
            date=request.data['date'],
            start_time=request.data['start_time'],
            end_time=request.data['end_time'],
            cancelled=False,
            cancelled_by_customer=False,
            cancelled_by_business=False,
            customer=customer,
            service=service,
            business=business
        )
        appointment.full_clean()

        days_open, opening_times, closing_times = get_business_hours(business)

        date = appointment.date
        start_time = appointment.start_time
        end_time = appointment.end_time

        new_start_date = datetime.datetime.combine(date, start_time)
        new_end_date = datetime.datetime.combine(date, end_time)
        day_of_week = date.weekday()
        opening_time = opening_times[day_of_week]
        closing_time = closing_times[day_of_week]
        duration = (new_end_date - new_start_date).seconds // 60
        days_between = (new_start_date - datetime.datetime.now()).days

        acceptable_minutes = []
        i = 0
        while (i*MIN_DURATION < 60):
            acceptable_minutes.append(i*MIN_DURATION)
            i += 1

        # Check that appointment date and time is valid
        if days_open[day_of_week] == False:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: business is closed on that date'})
        if days_between < 0:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: date has past'})
        if days_between > business.days_bookable_in_advance:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: date is too far in the future'})
        if start_time < opening_time:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: starting time is before opening time'})
        if end_time > closing_time:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: ending time is after closing time'})
        if start_time.minute not in acceptable_minutes or start_time.second != 0:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: start time is not at a valid miute'})
        if end_time.minute not in acceptable_minutes or end_time.second != 0:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: end time is not at a valid minute'})
        if duration != service.duration:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: appointment duration does not match service duration'})

        day_appointments = list(Appointment.objects.filter(business_id=request.data['business_id'], date=date).values('start_time', 'end_time').order_by('start_time'))

        # Make sure appointment does not conflict with existing appointments
        for existing_appointment in day_appointments:
            existing_start_date = datetime.datetime.combine(date, existing_appointment['start_time'])
            existing_end_date = datetime.datetime.combine(date, existing_appointment['end_time'])

            if new_start_date < existing_end_date and new_end_date > existing_start_date:
                return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Invalid: conflicts with existing appoitments'})

        appointment.save()

        serializer = ServiceSerializer(service, many=False)
        return JsonResponse(serializer.data, safe=False)

    except Exception:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'status':'false', 'message':'Bad request'})

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def business_cancel_appointment(request, business_id, appointment_id):
    authenticate_business(request, business_id)

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

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def customer_cancel_appointment(request, customer_id, appointment_id):
    authenticate_customer(request, customer_id)

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
