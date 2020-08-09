from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'businesses', views.BusinessViewSet, 'businesses')
router.register(r'services', views.ServiceViewSet, 'services')
router.register(r'appointments', views.AppointmentViewSet, 'appointments')

# app_name = 'booking'
urlpatterns = [
    path('', include(router.urls)),

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
