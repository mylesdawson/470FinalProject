from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from booking import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'customers', views.CustomerViewSet)
# router.register(r'businesses', views.BusinessViewSet)
# router.register(r'services', views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', rest_views.obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
