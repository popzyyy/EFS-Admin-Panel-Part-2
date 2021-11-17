import datetime

from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import get_user_model
#from application.utils import render_to_pdf
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
now = timezone.now()
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout as bruh
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
from fpdf import *
from django.core.mail import EmailMessage


def food_menu(request):
    return render(request, 'food_menu.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html', )


def login(request):
    return render(request, 'registration/login.html')


@login_required
def logout1(request):
    bruh(request)
    return render(request, 'registration/logout.html')

'''
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        cum = str(Movie.objects.values('movie_id'))
        template = get_template('movie_list.html')
        context = {
            'ID': test
        }
        html = template.render(context)
        pdf = render_to_pdf(context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            content = "inline; filename='fart"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
'''


@login_required
def export_pdf(request):
    movies = Movie.objects.all()

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Helvetica','', 20)
    pdf.cell(70, 10, 'Sigma Alpha Beta Movie Listings', 0, 1,)
    pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('courier', '', 11)
    pdf.cell(280, 8, f"{'Name'.ljust(28)}  {'Rating'.ljust(11)} {'Length'.ljust(11)} "
                     f"{'Genre'.ljust(11)} {'Available Date'.ljust(20)}", 0, 1)

    pdf.line(10, 38, 280, 38)
    for movie in movies:
        movie.length_min = str(movie.length_min)
        movie.available_date = datetime.datetime.now().date()
        movie.available_date = str(movie.available_date)

        pdf.cell(280, 8, f"{movie.name.ljust(28)}  "
                         f"{movie.rating.ljust(11)} "
                         f"{movie.length_min.ljust(11)} "
                         f"{movie.genre.ljust(18)} "
                         f"{movie.available_date.ljust(20)}", 0, 1)

    pdf.output('SAB_Movies.pdf', 'F')
    return FileResponse(open('SAB_Movies.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


@login_required
def email_pdf(request):
    movies = Movie.objects.all()

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Helvetica','', 20)
    pdf.cell(10, 10, 'Sigma Alpha Beta Movie Listings', 0, 1)
    pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('courier', '', 11)
    pdf.cell(280, 8, f"{'Name'.ljust(28)}  {'Rating'.ljust(11)} {'Length'.ljust(11)} "
                     f"{'Genre'.ljust(11)} {'Available Date'.ljust(20)}", 0, 1)

    pdf.line(10, 38, 280, 38)
    for movie in movies:
        movie.length_min = str(movie.length_min)
        movie.available_date = datetime.datetime.now().date()
        movie.available_date = str(movie.available_date)

        pdf.cell(280, 8, f"{movie.name.ljust(28)}  "
                         f"{movie.rating.ljust(11)} "
                         f"{movie.length_min.ljust(11)} "
                         f"{movie.genre.ljust(18)} "
                         f"{movie.available_date.ljust(20)}", 0, 1)

    pdf.output('SAB_Movies.pdf', 'F')
    user = request.user
    email_msg = EmailMessage(
        'Movie Report',
        'A list of movies here at Sigma Alpha Beta Movies. Visit soon!',
        'popzyyy0@gmail.com',
        [user.email],
        reply_to=['another@example.com'],
        headers={'Message-ID': 'foo'},
    )
    email_msg.attach_file('SAB_Movies.pdf')
    email_msg.send()
    context = {}
    return render(request, 'movie_list_confirmed.html', context=context)

@login_required()
def movie_list_confirmed(request):

    return render(request, 'movie_list.html')
@login_required
def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            bruh = form.save(commit=False)
            bruh.created_date = timezone.now()
            bruh.save()
            bruhplural = Movie.objects.filter(created_date__lte=timezone.now())

            movie_name = form.cleaned_data["name"]
            movie_length_min = form.cleaned_data["length_min"]
            movie_length_min = str(movie_length_min)
            movie_genre = form.cleaned_data["genre"]
            movie_rating = form.cleaned_data["rating"]
            movie_available_date = form.cleaned_data["available_date"]

            movie = Movie()

            movie.name = movie_name
            movie.length_min = movie_length_min
            movie.genre = movie_genre
            movie.rating = movie_rating
            movie.available_date = movie_available_date

            movie.save()
            return render(request, 'movie_list.html',
                          {'bruhplural': bruhplural})
    else:
        form = MovieForm()

    return render(request, 'movie_new.html', {'form': form})


@login_required
def movie_list(request):
    movie = Movie.objects.filter(created_date__lte=timezone.now())
    return render(request, 'movie_list.html',
                  {'movies': movie})


@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.updated_date = timezone.now()
            movie.save()
            movie = Movie.objects.filter(created_date__lte=timezone.now())
            return render(request, 'movie_list.html',
                          {'movies': movie})
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_edit.html', {'form': form})


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')


@login_required
def theater_new(request):
    if request.method == "POST":
        form = TheaterForm(request.POST)
        if form.is_valid():
            bruh = form.save(commit=False)
            bruh.created_date = timezone.now()
            bruh.save()
            bruhplural = Theater.objects.filter(created_date__lte=timezone.now())
            return render(request, 'theater_list.html',
                          {'bruhplurals': bruhplural})
    else:
        form = TheaterForm()

    return render(request, 'theater_new.html', {'form': form})


@login_required
def theater_list(request):
    theater = Theater.objects.filter(created_date__lte=timezone.now())
    return render(request, 'theater_list.html', {'theaters': theater})


@login_required
def theater_edit(request, pk):
    theater = get_object_or_404(Theater, pk=pk)
    if request.method == "POST":
        form = TheaterForm(request.POST, instance=theater)
        if form.is_valid():
            theater = form.save(commit=False)
            theater.updated_date = timezone.now()
            theater.save()
            theater = Theater.objects.filter(created_date__lte=timezone.now())
            return render(request, 'theater_list.html',
                          {'theaters': theater})
    else:
        form = TheaterForm(instance=theater)
    return render(request, 'theater_edit.html', {'form': form})


@login_required
def theater_delete(request, pk):
    bruh = get_object_or_404(Theater, pk=pk)
    bruh.delete()
    return redirect('application:theater_list')


@login_required
def ticket_list(request):
    ticket = Ticket.objects.filter(created_date__lte=timezone.now())
    return render(request, 'ticket_list.html',
                  {'tickets': ticket})


@login_required
def ticket_new(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_date = timezone.now()
            ticket.save()
            tickets = Ticket.objects.filter(created_date__lte=timezone.now())
            return render(request, 'ticket_list.html',
                          {'tickets': tickets})
    else:
        form = TicketForm()
    return render(request, 'ticket_new.html', {'form': form})


@login_required
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.updated_date = timezone.now()
            ticket.save()
            ticket = Ticket.objects.filter(created_date__lte=timezone.now())
            return render(request, 'ticket_list.html',
                          {'tickets': ticket})
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_edit.html', {'form': form})


@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return redirect('application:ticket_list')


@login_required
def showtime_delete(request, pk):
    showtime = get_object_or_404(Showtime, pk=pk)
    showtime.delete()
    return redirect('application:showtime_list')


@login_required
def showtime_new(request):
    if request.method == "POST":
        form = ShowtimeForm(request.POST)
        if form.is_valid():
            showtime = form.save(commit=False)
            showtime.created_date = timezone.now()
            showtime.save()
            showtimes = Showtime.objects.filter(created_date__lte=timezone.now())
            return render(request, 'showtime_list.html',
                          {'showtimes': showtimes})
    else:
        form = ShowtimeForm()
    return render(request, 'showtime_new.html', {'form': form})


@login_required
def showtime_list(request):
    showtime = Showtime.objects.filter(created_date__lte=timezone.now())
    return render(request, 'showtime_list.html',
                  {'showtimes': showtime})


@login_required
def showtime_edit(request, pk):
    showtime = get_object_or_404(Showtime, pk=pk)
    if request.method == "POST":
        form = ShowtimeForm(request.POST, instance=showtime)
        if form.is_valid():
            showtime = form.save(commit=False)
            showtime.updated_date = timezone.now()
            showtime.save()
            showtime = Showtime.objects.filter(created_date__lte=timezone.now())
            return render(request, 'showtime_list.html',
                          {'showtimes': showtime})
    else:
        form = ShowtimeForm(instance=showtime)
    return render(request, 'showtime_edit.html', {'form': form})
