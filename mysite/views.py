from django.shortcuts import render
from django.http import HttpResponse
from .models import Votes, Restaurant
from django.template import loader


def index(request):
    vote_list = Votes.objects.order_by('-pub_date')[1:]
    template = loader.get_template('mysite/index.html')
    context = {
        'vote_list': vote_list
    }
    return HttpResponse(template.render(context, request))


def votes(requests):
    restaurant_list = Restaurant.objects.order_by('-name')
    template = loader.get_template('mysite/restaurants.html')
    context = {
        'restaurant_list': restaurant_list
    }
    return HttpResponse(template.render(context, requests))


def vote_desc(requests, restaurant_id):
    return HttpResponse(f"Restaurant vote:{restaurant_id}")


def vote(requests, restaurant_id):
    return HttpResponse(f"You made a vote for restaurant {restaurant_id} ")

