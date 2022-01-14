from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Hello"
    return HttpResponse(name)


def test(request):

    a = 10
    b = 10
    return HttpResponse(f"10 * 10 is {a*b}")
