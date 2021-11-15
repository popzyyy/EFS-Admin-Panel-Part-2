from django.contrib import admin

from application.models import Ticket, Movie, Theater, Showtime


class TicketList(admin.ModelAdmin):
    list_display = ('price', 'type', 'matinee', 'sold_date', 'showtime', 'movie', 'theater')
    list_filter = ('price', 'type', 'matinee', 'sold_date', 'showtime', 'movie', 'theater')
    search_fields = ('price', 'type', 'matinee', 'sold_date', 'showtime', 'movie', 'theater')
    # ordering = ['id']


class MovieList(admin.ModelAdmin):
    list_display = ('movie_id', 'name', 'length_min', 'genre', 'rating', 'available_date')
    list_filter = ('movie_id', 'name', 'length_min', 'genre', 'rating', 'available_date')
    search_fields = ('movie_id', 'name', 'length_min', 'genre', 'rating', 'available_date')
    # ordering = ['id']


class ShowtimeList(admin.ModelAdmin):
    list_display = ('showtime_id', 'movies', 'theater', 'start_time', 'end_time')
    list_filter = ('showtime_id', 'movies', 'theater', 'start_time', 'end_time')
    search_fields = ('showtime_id', 'movies', 'theater', 'start_time', 'end_time')
    #ordering = ['id']


class TheaterList(admin.ModelAdmin):
    list_display = ('theater_id', 'room_number', 'capacity', 'available')
    list_filter = ('theater_id', 'room_number', 'capacity', 'available')
    search_fields = ('theater_id', 'room_number', 'capacity', 'available')
    # ordering = ['id']


admin.site.register(Theater, TheaterList)
admin.site.register(Showtime, ShowtimeList)
admin.site.register(Ticket, TicketList)
admin.site.register(Movie, MovieList)
