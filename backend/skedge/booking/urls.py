from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'businesses', views.BusinessViewSet, 'businesses')
router.register(r'services', views.ServiceViewSet, 'services')
router.register(r'appointments', views.AppointmentViewSet, 'appointments')

# app_name = 'booking'
urlpatterns = [
    path('', include(router.urls)),

    # Login to an account and return an authentication token
    path('login/', views.Login.as_view(), name='api_token_auth'),

    # Logout of an account and destroy the token
    path('logout/', views.Logout.as_view()),

    # CSRF token
    url(r'^get-token/$', views.get_csrf_token),

    # Get the information of a business
    path('business/<int:business_id>/', views.business_info),

    # Get the favorited businesses of a customer
    # Requires customer authentication
    path('favorites/<int:customer_id>/', views.favorite_businesses),

    # Add a favorite business for a customer
    # Requires customer authentication
    path('favorites/<int:customer_id>/add/<int:business_id>/', views.add_favorite_business),

    # Remove a favorite business for a customer
    # Requires customer authentication
    path('favorites/<int:customer_id>/remove/<int:business_id>/', views.remove_favorite_business),



    # Get the appointments for a customer
    # Requires customer authentication
    path('customer/<int:customer_id>/appointments/', views.customer_appointments),

    # Cancel an appointment by a customer
    # Requires customer authentication
    path('customer/<int:customer_id>/appointments/<int:appointment_id>/cancel/', views.customer_cancel_appointment),

    # Edit the main information of a business
    # Requires business authentication
    path('business/<int:business_id>/edit/main/', views.edit_main_business_info),

    # Edit the location information of a business
    # Requires business authentication
    path('business/<int:business_id>/edit/location', views.edit_location_business_info),

    # Edit the hours information of a business
    # Requires business authentication
    path('business/<int:business_id>/edit/hours', views.edit_hours_business_info),

    # Get the services offered by a business
    path('business/<int:business_id>/services/', views.business_services),

    # Create a service
    path('business/<int:business_id>/services/new', views.new_business_service),

    # Delete a service
    # Requires business authentication
    path('business/<int:business_id>/services/<int:service_id>/delete', views.delete_business_service),


    # Get the available appointment time slots for each service for a business for a specific day
    path('business/<int:business_id>/services/available/<int:year>/<int:month>/<int:day>/', views.services_available_times),

    # Get the available appointment days for a business for a specific month
    path('business/<int:business_id>/services/available/<int:year>/<int:month>/', views.services_available_days),

    # Get the appointments booked for a day for a business
    # Requires business authentication
    path('business/<int:business_id>/appointments/day/<int:year>/<int:month>/<int:day>/', views.business_appointments_by_day),

    # Get the appointments booked for a week for a business
    # Requires business authentication
    path('business/<int:business_id>/appointments/week/<int:year>/<int:week>/', views.business_appointments_by_week),

    # Cancel an appointment by a business
    # Requires business authentication
    path('business/<int:business_id>/appointments/<int:appointment_id>/cancel/', views.business_cancel_appointment),

    # Search for all businesses in a certain category
    path('business/search/<str:category>/', views.businesses_by_category),

    # Search for all businesses in a certain category whose names start with a search term
    path('business/search/<str:category>/<str:search>/', views.businesses_search),

]
