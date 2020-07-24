from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='login'),
    path('customer/new', views.new_customer, name='new'),
    path('business/new', views.new_business, name='new'),
    path('customer/edit', views.edit_customer, name='new'),
    path('business/edit', views.edit_business, name='new'),


    path('appointment/new', views.new_appointment)
    path('appointment/edit', views.edit_appointment)

    # path('<int:contact_id>/', views.detail, name='detail'),
    # path('<int:contact_id>/edit', views.edit, name='edit'),
]
