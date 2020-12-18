from django.shortcuts import render
from django.views.generic import ListView
from .models import MovieUnit

# Create your views here.
def test_view(request):
    return render(request, 'index.html', {})

class MovieUnitList(ListView):
    model = MovieUnit