"""Views for site."""
from django.shortcuts import render


# Create your views here.


def home_view(request):
    """Home view callable, for the home page."""
    return render(request, 'imagersite/home.html')


def login(request):
    """Login view callable, for the login page."""
    return render(request, 'imagersite/login.html')
