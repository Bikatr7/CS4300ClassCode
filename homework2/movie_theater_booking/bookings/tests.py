from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie, Seat, Booking
from datetime import date
import json

class MovieTheaterTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            duration=120,
            release_date=date.today()
        )

    def test_movie_creation_and_seats(self):
        """Test that movie creation automatically creates seats"""
        seats = self.movie.seats.all()
        self.assertEqual(seats.count(), 25)  ## 5x5 grid
        self.assertTrue(all(not seat.is_booked for seat in seats))

    def test_api_endpoints(self):
        """Test API endpoints return correct data"""
        ## Test movie listing
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Test Movie")

        ## Test seats endpoint
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 25)

    def test_booking_process(self):
        """Test the seat booking process"""
        seats = self.movie.seats.filter(is_booked=False)[:2]
        seat_ids = [seat.id for seat in seats]

        response = self.client.post(
            reverse('book_seat', args=[self.movie.id]),
            {'seats': seat_ids},
            follow=True
        )
        self.assertEqual(response.status_code, 200)

        for seat_id in seat_ids:
            seat = Seat.objects.get(id=seat_id)
            self.assertTrue(seat.is_booked)

        booking = Booking.objects.first()
        self.assertEqual(booking.seats.count(), 2)
        self.assertEqual(booking.movie, self.movie)

    def test_double_booking_prevention(self):
        """Test that seats cannot be double-booked"""
        seat = self.movie.seats.first()
        
        ## first booking
        response = self.client.post(
            reverse('book_seat', args=[self.movie.id]),
            {'seats': [seat.id]},
            follow=True
        )
        self.assertEqual(response.status_code, 200)

        ## Try to book the same seat again
        response = self.client.post(
            reverse('book_seat', args=[self.movie.id]),
            {'seats': [seat.id]},
            follow=True
        )
        self.assertContains(response, "Some selected seats are already booked")

    def test_web_interface(self):
        """Test web interface views"""
        ## Test movie listing page
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")

        ## Test booking page
        response = self.client.get(reverse('book_seat', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Screen")
        self.assertContains(response, "A1")

        ## Test booking history page
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)

    def test_movie_creation_form(self):
        """Test adding a new movie through the form"""
        movie_data = {
            'title': 'New Test Movie',
            'description': 'Another test movie',
            'duration': 150,
            'release_date': date.today()
        }
        response = self.client.post(reverse('add_movie'), movie_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        movie = Movie.objects.get(title='New Test Movie')
        self.assertEqual(movie.duration, 150)
        
        self.assertEqual(movie.seats.count(), 25)

    def test_booking_validation(self):
        """Test booking validation"""
        ## Test empty seat selection
        response = self.client.post(
            reverse('book_seat', args=[self.movie.id]),
            {'seats': []},
            follow=True
        )
        self.assertContains(response, "Please select at least one seat")

        ## Test invalid seat ID
        response = self.client.post(
            reverse('book_seat', args=[self.movie.id]),
            {'seats': [999]},
            follow=True
        )
        self.assertContains(response, "Some selected seats are no longer available")