from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Votes, Restaurant
from django.urls import reverse
from .forms import VoteForm, RestaurantForm, NewUserForm
from django.template import loader
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(requests):
    return render(requests, 'mysite/index.html')


def show_restaurants(requests):
    restaurants = Restaurant.objects.order_by('-name')
    context = {'restaurants': restaurants}
    return render(requests, 'mysite/restaurants.html', context)


def show_restaurant(requests, rid):
    restaurant = get_object_or_404(Restaurant, pk=rid)
    context = {'restaurant': restaurant}
    return render(requests, "mysite/test.html", context)


def add_restaurant(request):
    if request.method != "POST":
        form = RestaurantForm()
    else:
        form = RestaurantForm(request.POST)
        form.save()
    context = {'form': form}
    return render(request, 'mysite/add_restaurant.html', context)


def vote(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    print(restaurant)
    if request.method == 'GET':
        votes_form = VoteForm()

    if request.method == 'POST':
        votes_form = VoteForm(request.POST)
        votes_form.save()
    return render(request, 'mysite/voting.html', context={'restaurant': restaurant, 'form': votes_form})


def votes(request):
    show_votes = Votes.objects.all()
    return render(request, 'mysite/votes.html', {'vote': show_votes})


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('mysite:home')
        messages.error(request, 'invalid information')
    form = NewUserForm()
    return render(request, template_name="registration/register.html", context={'register_form': form})








