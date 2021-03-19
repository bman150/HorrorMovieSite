from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# HorrorSubGenre describes the subgenre name and a summary about it.
class HorrorSubGenre(models.Model):
    genrename=models.CharField(max_length=255)# name of horror subgenre
    genredescription=models.TextField(null=True, blank=True)# description of horror subgenre

    # __str__ (toString method)
    def __str__(self):
        return self.genrename
    # subclass
    class Meta:
        db_table='horrorsubgenre'
        verbose_name_plural='horrorsubgenres'
# Movie describes the movie title, year of release, subgenre name, director and summary of the movie.
class Movie(models.Model):
    movietitle=models.CharField(max_length=255)# title of the movie
    horrorsubgenre=models.Foreignkey(HorrorSubGenre, on_delete=models.DO_NOTHING)# subgenrea of the movie
    user=models.Foreignkey(User, on_delete=models.DO_NOTHING)# user who posts the movie information
    moviereleasedate=models.DateField()# release date of the movie
    moviedirector=models.CharField(max_length=255)# director of the movie
    moviedescription=models.TextField(null=True, blank=True) # summary about the movie

    def __str__(self):
        return self.movietitle

    class Meta:
        db_table='movie'
        verbose_name_plural='movies'