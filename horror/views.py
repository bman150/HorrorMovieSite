from django.shortcuts import render
from .models import HorrorSubGenre, Movie

# Create your views here.
# Return index for horror app.
def index(request):
    return render(request, 'horror/index.html') 

# Retrieves all the horror sub-genres.
def genres(request):
    genre_list=HorrorSubGenre.objects.all() 
    return render(request, 'horror/genres.html', {'genre_list' : genre_list})

# Retrieves all the horror movies
def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'horror/movies.html', {'movie_list' : movie_list})