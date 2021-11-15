from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Theater(models.Model):
    theater_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    available = models.BooleanField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.theater_id)


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    length_min = models.IntegerField()
    genre = models.CharField(max_length=25)
    rating = models.CharField(max_length=4)
    available_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)

    def available(self):
        self.available_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.movie_id)


class Showtime(models.Model):
    showtime_id = models.AutoField(primary_key=True)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='theater')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.showtime_id)


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='showtime')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    types = (
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
        ('Member', 'Member')
    )
    type = models.CharField(
        max_length=32,
        choices=types,
    )
    matinee = models.BooleanField()

    sold_date = models.DateTimeField(auto_now_add=True)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ticket_id)
