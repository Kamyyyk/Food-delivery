from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('restaurants/', views.restaurant_detail, name='restaurants'),
    path('restauracje/<restaurant_id>', views.show_restaurant, name='restauracje'),
    path('jsontest/', views.test, name='test')
]

