from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()  ## minutes (probably)

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"

    class Meta:
        unique_together = ['movie', 'seat_number']  ## Ensure unique seat numbers per movie

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        seat_numbers = ", ".join([seat.seat_number for seat in self.seats.all()])
        return f"{self.movie.title} - Seats: {seat_numbers}"

@receiver(post_save, sender=Movie)
def create_seats(sender, instance, created, **kwargs):
    if(created):
        rows = 'ABCDE'
        cols = range(1, 6)
        
        for row in rows:
            for col in cols:
                seat_number = f"{row}{col}"
                Seat.objects.create(
                    movie=instance,
                    seat_number=seat_number
                )
