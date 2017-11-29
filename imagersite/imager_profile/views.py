"""Views for site."""
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def home_view(request):
    """Home view callable, for the home page."""
    return render(request, 'imagersite/home.html')


# def log_in(request):
#     """Log in view callable, for log in page."""
#     return render(request, 'imagersite/log_in.html')


# def log_out(request):
#     """Log out view callable, for log out page."""
#     return render(request, 'imagersite/log_out.html')
