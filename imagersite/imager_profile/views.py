"""Views for site."""
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def home_view(request):
    """Home view callable, for the home page."""
    return render(request, 'imagersite/home.html')
