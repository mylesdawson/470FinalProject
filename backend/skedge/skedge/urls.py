from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from booking import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'businesses', views.BusinessViewSet, 'businesses')
router.register(r'services', views.ServiceViewSet, 'services')
router.register(r'appointments', views.AppointmentViewSet, 'appointments')

urlpatterns = [
    path('', include(router.urls)),

    # This is essentially our login. It will return a token if login was successful
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', views.Logout.as_view()),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('booking.urls')),
]
