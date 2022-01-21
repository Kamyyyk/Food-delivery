from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('restaurants/', views.restaurant_detail, name='restaurants'),
    path('votes/<votes_id>', views.test, name='votes'),
    # path('voteid/<int:restaurant_id>/', views.vote_desc, name='voteid'),
    # path('vote/<int:restaurant_id>/', views.vote, name='vote'),

]

