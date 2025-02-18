from django.test import TestCase
from .models import Movie
from datetime import date

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(
            title="Test Movie",
            description="A sample description",
            duration=120,
            release_date=date.today()
        )

    def test_movie_creation(self):
        movie = Movie.objects.get(title="Test Movie")
        self.assertEqual(movie.duration, 120)
