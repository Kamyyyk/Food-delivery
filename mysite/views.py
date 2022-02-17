from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Votes, Restaurant
from django.urls import reverse
from .forms import VoteForm, RestaurantForm, NewUserForm, UserCreationForm
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
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added new restaurant")
            return redirect('mysite:add')
        messages.error(request, "Error")
    form = RestaurantForm()
    context = {'form': form}
    return render(request, 'mysite/add_restaurant.html', context)


def edit_restaurant(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant_form = RestaurantForm(instance=restaurant)

    if request.method == "GET":
        restaurant_form = RestaurantForm(instance=restaurant)

    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST, instance=restaurant)
        if restaurant_form.is_valid():
            restaurant_form.save()
            return HttpResponseRedirect(reverse('mysite:restaurants'))
    context = {'form': restaurant_form, 'restaurant': restaurant}
    return render(request, 'mysite/edit_restaurant.html', context)


def delete_restaurant(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.delete()
    return redirect('mysite:restaurants')


def register_request(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Created account {user}')
            return redirect('login')
    return render(request, template_name="registration/register.html", context={'register_form': form})


def login_request(request):
    if request.user.is_authenticated:
        return redirect('mysite:home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mysite:home')
        else:
            messages.info(request, "Login albo haslo sa bledne")

    return render(request, 'registration/login.html', context={})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('mysite:home')


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
