from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Haslo',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label='Potwierdz haslo',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Nazwa uzytkownika',
            'email': 'E-mail',
            'password1': 'Haslo',
            'password2': 'Powtorz haslo',
        }

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = field = [
            'name',
            'place',
            'category'
        ]
        labels = {
            'name': 'Nazwa',
            'place': 'Miejsce',
            'category': 'Kategoria',

        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'
