from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Hello"
    return HttpResponse(name)