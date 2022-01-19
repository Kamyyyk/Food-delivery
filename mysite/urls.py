from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('votes/', views.detail, name='detail'),
    # path('detail/<int:restaurant_id>', views.detail, name='detail'),
    path('voteid/<int:restaurant_id>/', views.vote_desc, name='voteid'),
    path('vote/<int:restaurant_id>/', views.vote, name='vote'),

]

