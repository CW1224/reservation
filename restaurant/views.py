from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking

# Create your views here.

def open_home_page(request):
    return render(request, 'restaurant/base.html')

def menu_show(request):
    return render(request, 'restaurant/menu.html')