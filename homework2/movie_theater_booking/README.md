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

## API Endpoints

- /api/movies/ - List and manage movies
- /api/seats/ - List and manage seats
- /api/bookings/ - List and manage bookings

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

## Notes

- The system allows anonymous bookings (no login required)
- Each movie has its own set of seats
- Multiple seats can be booked in a single transaction
- Seats are automatically created when a movie is added
- The booking system is protected against race conditions