
from django.urls import re_path
from django.urls import path
from application import views
from .views import SignUpView

app_name = 'application'
urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),

    path('food_menu/', views.food_menu, name='food_menu'),


    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout1, name='logout'),
    re_path(r'^home/$', views.home, name='home'),

    #path('GeneratePdf/', GeneratePdf.as_view(), name='generatepdf'),
    path('export_pdf/', views.export_pdf, name='exportpdf'),
    path('email_pdf/', views.email_pdf, name='emailpdf'),
    path('email_pdf/', views.movie_list_confirmed, name='movie_list_confirmed'),


    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('movie/new/', views.movie_new, name='movie_new'),
    path('accounts/profile/', views.home, name='home'),

    path('theater_list/', views.theater_list, name='theater_list'),
    path('theater/<int:pk>/edit/', views.theater_edit, name='theater_edit'),
    path('theater/<int:pk>/delete/', views.theater_delete, name='theater_delete'),
    path('theater/new/', views.theater_new, name='theater_new'),

    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('ticket/<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
    path('ticket/new/', views.ticket_new, name='ticket_new'),

    path('showtime_list/', views.showtime_list, name='showtime_list'),
    path('showtime/<int:pk>/edit/', views.showtime_edit, name='showtime_edit'),
    path('showtime/<int:pk>/delete/', views.showtime_delete, name='showtime_delete'),
    path('showtime/new/', views.showtime_new, name='showtime_new'),

    path('food_menu/', views.food_menu, name='food_menu'),

]
