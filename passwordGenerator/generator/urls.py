from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('creator/', views.creator, name='creator'),
    path('form/', views.password_form, name='password_form'),
    path('password/', views.generate_password, name='generate_password'),
]
