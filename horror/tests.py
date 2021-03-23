from django.test import TestCase
from .models import HorrorSubGenre, Movie
from .forms import HorrorSubGenreForm, MovieForm


class HorrorSubGenreTest(TestCase):
    def setUp(self):
        self.genre=HorrorSubGenre(genrename='Haunted House')

    def test_typestring(self):
        self.assertEqual(str(self.genre), 'Haunted House')

    def test_tablename(self):
        self.assertEqual(str(HorrorSubGenre._meta.db_table), 'horrorsubgenre')


class MovieTest(TestCase):
    def setUp(self):
        self.title=Movie(movietitle='The Hills Have Eyes')

    def test_typestring(self):
        self.assertEqual(str(self.title), 'The Hills Have Eyes')

    def test_tablename(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

# Form tests
class HorrorSubGenre_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=HorrorSubGenreForm(data={'genrename': "genre1", 'genredescription' : "some genre"})
        self.assertTrue(form.is_valid())