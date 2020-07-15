from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:contact_id>/edit_contact', views.edit_contact, name='edit_contact'),
    path('new/', views.NewView.as_view(), name='new'),
    path('new/add_content', views.add_contact, name='add_contact'),
]