# films/views.py
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_films')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def view_films(request):
    films = Film.objects.all()
    return render(request, 'films/view_films.html', {'films': films})

