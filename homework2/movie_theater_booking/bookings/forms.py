from django import forms
from .models import Movie, Seat

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': 'required'
        }),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'duration']

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['seat_number'] 