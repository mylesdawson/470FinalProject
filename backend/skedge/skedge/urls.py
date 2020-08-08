from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from booking import views



urlpatterns = [

    # This is essentially our login. It will return a token if login was successful
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', views.Logout.as_view()),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('booking.urls')),
]
