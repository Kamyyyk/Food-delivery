from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('votes/', views.votes, name='detail'),
    path('voteid/<int:restaurant_id>/', views.vote_desc, name='voteid'),
    path('vote/<int:restaurant_id>/', views.vote, name='vote'),

]

