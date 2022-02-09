from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Votes, Restaurant
from django.template import loader
from django.http import Http404
from django.contrib.auth import authenticate, login, logout


def home(requests):
    return render(requests, 'mysite/not_logged.html')


def index(request):
    return render(request, 'mysite/home.html')


def logout(request):
    return render(request, 'mysite/not_logged.html')


def show_restaurants(requests):
    restaurants = Restaurant.objects.order_by('-name')
    context = {'restaurants': restaurants}
    return render(requests, 'mysite/restaurants.html', context)


def show_restaurant(requests, rid):
    restaurant = get_object_or_404(Restaurant, pk=rid)
    context = {'restaurant': restaurant}
    return render(requests, "mysite/test.html", context)


def login(request):
    return render(request, 'mysite/login.html')


def register(request):
    return render(request, 'mysite/register.html')







