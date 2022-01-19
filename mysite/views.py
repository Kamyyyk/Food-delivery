from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Hello"
    return HttpResponse(name)


def detail(requests, restaurant_id):
    return HttpResponse(f'Restaurant nr: {restaurant_id}')


def vote_desc(requests, restaurant_id):
    return HttpResponse(f"Restaurant vote:{restaurant_id}")


def vote(requests, restaurant_id):
    return HttpResponse(f"You made a vote for restaurant {restaurant_id} ")


