from django.forms import ModelForm
from .models import *


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class VoteForm(ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'
