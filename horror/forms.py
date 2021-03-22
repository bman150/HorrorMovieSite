from django import forms
from .models import HorrorSubGenre, Movie

class HorrorSubGenreForm(forms.ModelForm):
    class Meta:
        model=HorrorSubGenre
        fields='__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'