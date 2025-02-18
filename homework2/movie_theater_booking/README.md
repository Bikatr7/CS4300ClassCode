# Movie Theater Booking System

A Django-based movie theater booking system that provides both a REST API and web interface for managing movie bookings.

## Features

- View movie listings
- Book multiple seats for movies
- Automatic seat grid generation (5x5) for each movie
- Check booking history
- RESTful API endpoints
- User-friendly web interface using Bootstrap

## Setup Instructions

Note: I am on Mac, your commands may vary.

0. Get into the directory:
cd homework2/movie_theater_booking

1. Create and activate a virtual environment (optional):
python3 -m venv myenv --system-site-packages
source myenv/bin/activate

2. Install dependencies:
pip3 install -r requirements.txt

3. Run migrations:
python3 manage.py makemigrations
python3 manage.py migrate

4. Start the development server:
python3 manage.py runserver localhost:3000

5. Access the application:
- Web Interface: http://localhost:3000/
- API Endpoints: http://localhost:3000/api/

## API Documentation

### Movies

GET /api/movies/
Response:
[
    {
        "id": 1,
        "title": "Example Movie",
        "description": "A great movie",
        "release_date": "2024-02-18",
        "duration": 120
    }
]

POST /api/movies/
Request:
{
    "title": "New Movie",
    "description": "Another great movie",
    "release_date": "2024-02-18",
    "duration": 150
}

### Seats

GET /api/seats/
Response:
[
    {
        "id": 1,
        "movie": 1,
        "seat_number": "A1",
        "is_booked": false
    }
]

### Bookings

GET /api/bookings/
Response:
[
    {
        "id": 1,
        "movie": 1,
        "seats": [1, 2],
        "booking_date": "2024-02-18T22:00:00Z"
    }
]

POST /api/bookings/
Request:
{
    "movie": 1,
    "seats": [1, 2]
}

## Web Interface URLs

- / - Movie listing
- /movie/add/ - Add new movies
- /book/<movie_id>/ - Book seats for a specific movie
- /history/ - View booking history

## Key Features

### Automatic Seat Creation
- When a new movie is added, a 5x5 grid of seats (A1-E5) is automatically created
- Each movie has its own independent set of seats

### Seat Booking System
- Multiple seats can be selected and booked in one transaction
- Visual seat grid showing available and booked seats
- Real-time seat status updates
- Protection against double-booking through database locks
- Transaction-based booking to ensure data consistency

### Booking Validation
- Server-side validation of seat availability
- Race condition prevention using select_for_update
- Atomic transactions for booking multiple seats
- Clear error messages for booking failures

## Project Structure

- bookings/ - Main application directory
  - models.py - Database models (Movie, Seat, Booking)
  - views.py - View logic and booking handling
  - urls.py - URL routing
  - serializers.py - API serializers
  - forms.py - Form definitions
  - templates/ - HTML templates
    - base.html - Base template with common styling
    - movie_list.html - Movie listing
    - seat_booking.html - Interactive seat booking interface
    - booking_history.html - Booking records
    - add_movie.html - Movie creation form

## Testing

Run all tests:
python3 manage.py test

Run specific test case:
python3 manage.py test bookings.tests.MovieTheaterTests

Run specific test method:
python3 manage.py test bookings.tests.MovieTheaterTests.test_booking_process

Run tests with more detail:
python3 manage.py test -v 2

The tests verify:
- Movie creation with automatic seat generation
- API endpoints functionality
- Multiple seat booking process
- Prevention of double-booking
- Web interface functionality
- Movie creation through forms
- Booking validation
- Error handling

## Notes

- The system allows anonymous bookings (no login required)
- Each movie has its own set of seats
- Multiple seats can be booked in a single transaction
- Seats are automatically created when a movie is added
- The booking system is protected against race conditions