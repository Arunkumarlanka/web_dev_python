from django.urls import path  
from homee import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('prediction/', views.prediction, name='prediction'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]