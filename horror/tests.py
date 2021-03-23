from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from .models import HorrorSubGenre, Movie
from .forms import HorrorSubGenreForm, MovieForm


class HorrorSubGenreTest(TestCase):
    def setUp(self):
        self.genre=HorrorSubGenre(genrename='Haunted House', genredescription="A house haunted by a ghost")

    def test_string(self):
        self.assertEqual(str(self.genre), 'Haunted House')

    def test_tablename(self):
        self.assertEqual(str(HorrorSubGenre._meta.db_table), 'horrorsubgenre')


class MovieTest(TestCase):
    def setUp(self):
        self.genre=HorrorSubGenre(genrename='Haunted House')
        self.user=User(username='user1')
        self.movie=Movie(movietitle='A House on Haunted Hill', horrorsubgenre=self.genre, user=self.user, moviereleasedate=datetime.date(1959, 2, 17), moviedirector='William Castle', moviedescription="A millionaire offers $10,000 to five people who agree to be locked in a large, spooky, rented house overnight with him and his wife.")

    def test_string(self):
        self.assertEqual(str(self.movie), 'A House on Haunted Hill')


    def test_tablename(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

# Form tests
class HorrorSubGenre_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=HorrorSubGenreForm(data={'genrename': "genre1", 'genredescription' : "some genre"})
        self.assertTrue(form.is_valid())