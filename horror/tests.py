from django.test import TestCase
from .models import HorrorSubGenre, Movie

# Create your tests here.
class HorrorSubGenreTest(TestCase):
    def setUp(self):
        self.genre=HorrorSubGenre(genrename='Haunted House')

    def test_typestring(self):
        self.assertEqual(str(self.genre), 'Haunted House')

    def text_tablename(self):
        self.assertEqual(str(HorrorSubGenre._meta.db.table), 'horrorsubgenre')