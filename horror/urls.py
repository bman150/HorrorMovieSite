from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # register index view
    path('genres/', views.genres, name='genres'),
    path('movies/', views.movies, name='movies'),
    path('moviedetail/<int:id>', views.moviedetail, name='moviedetail'),
]