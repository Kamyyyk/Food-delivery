from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Votes, Restaurant
from django.http import Http404
from django.contrib.auth import authenticate, login


def index(requests):
    try:
        vote_list = Votes.objects.order_by('-pub_date')
    except Votes.DoesNotExist:
        raise Http404("Nie ma glosu o takim id...")
    context = {'vote_list': vote_list}
    return render(requests, 'mysite/index.html', context)


def restaurant_detail(requests):
    try:
        restaurants = Restaurant.objects.order_by('-name')
    except Votes.DoesNotExist:
        raise Http404("Nie ma restauracji o takim id")
    return render(requests, "mysite/restaurants.html", {'restaurants': restaurants})


def show_restaurant(requests, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(requests, "mysite/test.html", {'restaurant': restaurant})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('mysite:index')


