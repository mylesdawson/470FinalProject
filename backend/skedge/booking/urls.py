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

    # This is essentially our login. It will return a token if login was successful
    path('login/', views.Login.as_view(), name='api_token_auth'),
    path('logout/', views.Logout.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/$', views.get_csrf_token),

    path('business/<int:business_id>/', views.business_info),

    # Requires customer authentication
    path('favorites/<int:customer_id>/', views.favorite_businesses),
    # Requires customer authentication
    path('favorites/<int:customer_id>/add/<int:business_id>/', views.add_favorite_business),
    # Requires customer authentication
    path('favorites/<int:customer_id>/remove/<int:business_id>/', views.remove_favorite_business),

    # Requires customer authentication
    path('customer/<int:customer_id>/appointments/', views.customer_appointments),
    # Requires customer authentication
    path('customer/<int:customer_id>/appointments/<int:appointment_id>/cancel/', views.customer_cancel_appointment),

    path('business/<int:business_id>/edit/main/', views.edit_main_business_info),
    path('business/<int:business_id>/edit/location', views.edit_location_business_info),
    path('business/<int:business_id>/edit/hours', views.edit_hours_business_info),

    path('business/<int:business_id>/services/', views.business_services),

    path('business/<int:business_id>/services/available/<int:year>/<int:month>/<int:day>/', views.services_available_times),
    path('business/<int:business_id>/services/available/<int:year>/<int:month>/', views.services_available_days),

    path('business/<int:business_id>/appointments/day/<int:year>/<int:month>/<int:day>/', views.business_appointments_by_day),
    path('business/<int:business_id>/appointments/week/<int:year>/<int:week>/', views.business_appointments_by_week),

    # Requires business authentication
    path('business/<int:business_id>/appointments/<int:appointment_id>/cancel/', views.business_cancel_appointment),

    path('business/search/<str:category>/', views.businesses_by_category),
    path('business/search/<str:category>/<str:search>/', views.businesses_search),

]
