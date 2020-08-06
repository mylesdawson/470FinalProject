from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from booking import views

router = routers.DefaultRouter()
# router.register(r'register', views.UserCreate.as_view(), basename="UserCreate")
# router.register(r'users', views.UserViewSet)
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'businesses', views.BusinessViewSet, 'businesses')
# router.register(r'services', views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # This is essentially our login. It will return a token if login was successful
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', views.Logout.as_view()),

    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
