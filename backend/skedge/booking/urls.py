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

    path('favorites/<int:customer_id>', views.favorite_businesses),

    path('customer/<int:customer_id>/appointments/', views.customer_appointments),

    path('business/<int:business_id>/services/', views.business_services),

    path('business/<int:business_id>/services/available/<int:year>/<int:month>/<int:day>/', views.services_available_times),

    path('business/<int:business_id>/appointments/day/<int:year>/<int:month>/<int:day>/', views.business_appointments_by_day),
    path('business/<int:business_id>/appointments/week/<int:year>/<int:week>/', views.business_appointments_by_week),
    path('business/<int:business_id>/appointments/month/<int:year>/<int:month>/', views.business_appointments_by_month),

    path('business/search/<str:category>/', views.businesses_by_category),
    path('business/search/<str:category>/<str:search>/', views.businesses_search),

    # path('', views.index, name='index'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='login'),
    # path('customer/new', views.new_customer, name='new'),
    # path('business/new', views.new_business, name='new'),
    # path('customer/edit', views.edit_customer, name='new'),
    # path('business/edit', views.edit_business, name='new'),
    # path('appointment/new', views.new_appointment)
    # path('appointment/edit', views.edit_appointment)

]
