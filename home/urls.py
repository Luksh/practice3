from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path('services',services, name='services'),
    path('portfolio',portfolio, name='portfolio'),
    path('price',price, name='price'),
    path('contact',contact, name='contact'),


]
