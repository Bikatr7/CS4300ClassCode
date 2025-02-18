from rest_framework import viewsets
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Seat, Booking
from .seralizers import MovieSerializer, SeatSerializer, BookingSerializer

## API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

## Template Views
class MovieListView(ListView):
    model = Movie
    template_name = 'bookings/movie_list.html'
    context_object_name = 'movies'

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    available_seats = Seat.objects.filter(is_booked=False)
    
    if(request.method == 'POST'):
        seat_id = request.POST.get('seat')
        if(seat_id):
            seat = get_object_or_404(Seat, pk=seat_id)
            if(not seat.is_booked):
                booking = Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=request.user
                )
                seat.is_booked = True
                seat.save()
                messages.success(request, 'Seat booked successfully!')
                return redirect('booking_history')
            else:
                messages.error(request, 'This seat is already booked.')
        else:
            messages.error(request, 'Please select a seat.')
    
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': available_seats
    })

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })
