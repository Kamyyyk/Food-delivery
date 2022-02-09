from . import views
from django.urls import path

app_name = 'mysite'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('restaurant/<int:rid>', views.show_restaurant, name='restaurant'),
    path('restaurants', views.show_restaurants, name='restaurants'),
]

