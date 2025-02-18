from rest_framework import viewsets
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie, Seat, Booking
from .seralizers import MovieSerializer, SeatSerializer, BookingSerializer
from .forms import MovieForm

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

def add_movie(request):
    if(request.method == 'POST'):
        form = MovieForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('movie_list')
    else:
        form = MovieForm()
    
    return render(request, 'bookings/add_movie.html', {'form': form})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if(request.method == 'POST'):
        seat_ids = request.POST.getlist('seats')
        if(seat_ids):
            ## First check if any of these seats are already booked
            already_booked = Seat.objects.filter(
                id__in=seat_ids,
                movie=movie,
                is_booked=True
            ).exists()
            
            if(already_booked):
                messages.error(request, 'Some selected seats are already booked. Please refresh and try again.')
                return redirect('book_seat', movie_id=movie_id)
            
            seats = Seat.objects.filter(
                id__in=seat_ids,
                movie=movie,
                is_booked=False
            ).select_for_update() ## lock rows
            
            ## Verify we got all the seats we asked for
            if(len(seats) != len(seat_ids)):
                messages.error(request, 'Some selected seats are no longer available. Please try again.')
                return redirect('book_seat', movie_id=movie_id)
            
            try:
                ## atomicity transaction
                from django.db import transaction
                with transaction.atomic():
                    booking = Booking.objects.create(
                        movie=movie,
                        user=None
                    )
                    booking.seats.set(seats)
                    Seat.objects.filter(id__in=seat_ids).update(is_booked=True)
                    messages.success(request, 'Seats booked successfully!')
                    return redirect('booking_history')
            except Exception as e:
                messages.error(request, 'An error occurred while booking. Please try again.')
                return redirect('book_seat', movie_id=movie_id)
        else:
            messages.error(request, 'Please select at least one seat.')
    
    ## Organize seats into rows for the template
    seat_rows = {}
    for seat in movie.seats.all():
        row = seat.seat_number[0]
        if(row not in seat_rows):
            seat_rows[row] = []
        seat_rows[row].append(seat)
    
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seat_rows': seat_rows
    })

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })
