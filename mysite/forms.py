from django.forms import ModelForm
from .models import *


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        field = '__all__'


class VoteForm(ModelForm):
    class Meta:
        model = Votes
        field = '__all__'
