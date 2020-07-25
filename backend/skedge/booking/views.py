from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from .models import Customer, Business, Employee, Service, Appointment
from .serializers import CustomerSerializer, BusinessSerializer, ServiceSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet gives us all the common http actions on a model implicitly
    parser_classes = [JSONParser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request, pk=None):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            print(username)
            print(password)

            # TODO: This is always None for some reason
            user = authenticate(username=username, password=password)
            print(user)

            if user:
                # TODO: send a session token and login (can't get login to work rn)
                # login(user)
                print("user exists")
                token, _ = Token.objects.get_or_create(user=user)
                print("managed to make a token!")
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response('user is None!',status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'])
    def logout(self, request, pk=None):
        # TODO: test if this actually works
        logout(request)
        return Response(status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

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
