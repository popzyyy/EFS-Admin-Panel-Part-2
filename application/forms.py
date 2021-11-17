from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Movie, Theater, Ticket, Showtime, User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'length_min', 'genre', 'rating', 'available_date', 'created_date')
        date = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )


class TheaterForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = ('room_number', 'capacity', 'available', 'created_date')
        date = forms.DateField(
            widget=forms.TextInput(attrs={'type': 'date'}))

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('showtime', 'type', 'price', 'movie', 'theater', 'matinee', 'created_date')
        date = forms.DateField(
            widget=forms.TextInput(attrs={'type': 'date'}))

class ShowtimeForm(forms.ModelForm):
    class Meta:
        model = Showtime
        #length =
        #end_time = Movie.objects.filter(length_min=length)

        fields = ('movies', 'theater', 'start_time', 'end_time', 'created_date')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]
