from django.shortcuts import render
from django.http import HttpResponse
from .models import Votes, Restaurant
from django.http import Http404
from django.template import loader


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
        raise Http404("Nie ma takiej restauracji")
    return render(requests, "mysite/restaurants.html", {'restaurants': restaurants})


def test(requests, id):
    try:
        restaurant = Restaurant.objects.get(pk=id)
    except Restaurant.DoesNotExist:
        raise Http404("Nie ma takiej restauracji")
    return render(requests, "mysite/test.html", {'restaurant': restaurant})


# def votes(request):
#     restaurant_list = Restaurant.objects.order_by('-name')
#     context = {'restaurant_list': restaurant_list}
#     return render(request, 'mysite/restaurants.html', context)
#
#
# def vote_desc(requests, restaurant_id):
#     return HttpResponse(f"Restaurant vote:{restaurant_id}")
#
#
# def vote(requests, restaurant_id):
#     return HttpResponse(f"You made a vote for restaurant {restaurant_id} ")
