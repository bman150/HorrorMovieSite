from django.shortcuts import render, get_object_or_404
from .models import HorrorSubGenre, Movie
from .forms import HorrorSubGenreForm, MovieForm
from django.contrib.auth.decorators import login_required

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

# Detail view for horror movie sub-genres
def moviedetail(request, id):
    horrormovie=get_object_or_404(Movie, pk=id)
    context={
        'horrormovie' : horrormovie,
    }
    return render(request, 'horror/moviedetail.html', context=context)

# Create form functions here.
@login_required
def newHorrorSubGenre(request):
    form=HorrorSubGenreForm
    if request.method=='POST':
        form=HorrorSubGenreForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=HorrorSubGenreForm
    else:
        form=HorrorSubGenreForm()
    return render(request, 'horror/newhorrorsubgenre.html', {'form': form})

@login_required
def newMovie(request):
    form=MovieForm
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MovieForm
    else:
        form=MovieForm()
    return render(request, 'horror/newmovie.html', {'form': form})

# login and logout views
def loginmessage(request):
    return render(request, 'horror/loginmessage.html')

def logoutmessage(request):
    return render(request, 'horror/logoutmessage.html')