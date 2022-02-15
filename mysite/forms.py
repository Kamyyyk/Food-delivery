from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class VoteForm(ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'