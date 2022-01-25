from . import views
from django.urls import path

app_name = 'mysite'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login', views.my_view, name='login'),
    path('register', views.register, name='register'),
    path('restaurants/', views.restaurant_detail, name='restaurants'),
    path('restauracje/<restaurant_id>', views.show_restaurant, name='restauracje'),



]

