"""Views for site."""
from imager_profile.models import ImagerProfile
from imager_images.models import Album, Photo
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from random import choice


# Create your views here.


# def home_view(request):
#     """Home view callable, for the home page."""

#     return render(request, 'imagersite/home.html')


class HomeView(TemplateView):
    """Set up view for home page."""
    template_name = 'imagersite/home.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        photos = Photo.objects.filter(published='Public').all()
        if len(photos) > 0:
            context['photo'] = choice(photos)
        else:
            context['photo'] = None
        return context


class ProfileView(DetailView):
    """Private profile page view."""
    template_name = 'imagersite/profile.html'
    model = ImagerProfile
    context_object_name = 'profile'

    def get_object(self):
        """Get current user profile."""
        user = self.request.user.profile
        return user


class OtherProfileView(DetailView):
    """Set up profile view for other useres."""
    template_name = 'imagersite/profile.html'
    model = ImagerProfile
    slug_field = 'user__username'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    """View for editing the users profile."""
    template_name = 'imagersite/edit.html'
    model = ImagerProfile
    success_url = reverse_lazy('profile')
    fields = ['website', 'location', 'fee', 'camera', 'services', 'bio', 'phone_number', 'photo_style']

    def get_object(self):
        """Return the user."""
        return self.request.user.profile
