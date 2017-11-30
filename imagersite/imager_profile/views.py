"""Views for site."""
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home_view(request):
    """Home view callable, for the home page."""
    import pdb; pdb.set_trace()
    template = loader.get_template('imagersite/home.html')
    response_body = template.render({'name': 'Playa'})
    return HttpResponse(response_body)
