from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    ## API URLs
    path('api/', include(router.urls)),
    
    ## Template URLs
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movie/add/', views.add_movie, name='add_movie'),
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]
