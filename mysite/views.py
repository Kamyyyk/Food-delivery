from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Hello"
    return HttpResponse(name)


def detail(requests, restaurant_id):
    return HttpResponse(f'Restauracja nr {restaurant_id}')


def vote(requests, restaurant_id):
    return HttpResponse("You are vote for %s." % restaurant_id)


# def vote_desc(requests, vote_id):
#     return HttpResponse("" % vote_id,)
