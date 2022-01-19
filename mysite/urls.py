from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:restaurant_id>/detail/', views.detail, name='detail'),
    path('<int:restaurant_id>/vote/', views.vote, name='vote'),
    path('<int:vote_id>/vote/', views.vote_desc, name='vote'),

]

