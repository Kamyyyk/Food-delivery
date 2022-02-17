from . import views
from django.urls import path, include


app_name = 'mysite'
urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:rid>', views.show_restaurant, name='restaurant'),
    path('restaurants', views.show_restaurants, name='restaurants'),
    path('vote/<int:id>', views.vote, name='vote'),
    path('result', views.votes, name='result'),
    path('restaurant/add', views.add_restaurant, name='add'),
    path('restaurant/edit/<int:id>', views.edit_restaurant, name='edit_restaurant'),
    path('restaurant/delete/<int:id>', views.delete_restaurant, name="delete_restaurant"),

    path('account/register', views.register_request, name='register'),
    # path('account/login', views.login_request, name='login'),
    path('account/logout', views.logout, name='logout'),
]


