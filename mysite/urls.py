from . import views
from django.urls import path, include


app_name = 'mysite'
urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:rid>', views.show_restaurant, name='restaurant'),
    path('restaurants', views.show_restaurants, name='restaurants'),
    path('vote/<int:id>', views.vote, name='vote'),
    path('addrestaurant', views.add_restaurant, name='add'),
    path('result', views.votes, name='result'),

    path('register', views.register_request, name='register'),
]

