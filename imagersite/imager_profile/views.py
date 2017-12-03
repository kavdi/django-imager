"""Views for site."""
from django.shortcuts import render
from imager_profile.models import ImagerProfile
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from imager_profile.forms import ProfileForm
from django.http import HttpResponseRedirect


# Create your views here.


def home_view(request):
    """Home view callable, for the home page."""
    return render(request, 'imagersite/home.html')


def login(request):
    """Login view callable, for the login page."""
    return render(request, 'imagersite/login.html')


def register_view(request):
    """Register view callable."""
    return render(request)


# create profile view, library page, album view, photo view

class ProfileView(ListView):
    """Private profile page view."""

    template_name = 'imagersite/profile.html'
    model = ImagerProfile

    def get_context_data(self, **kwargs):
        """Setup page."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context['username'] = context['view'].request.user.profile.user
        context['website'] = context['view'].request.user.profile.website
        context['location'] = context['view'].request.user.profile.location
        context['fee'] = context['imagerprofile_list'][1].fee
        context['camera'] = context['imagerprofile_list'][1].camera
        context['services'] = context['imagerprofile_list'][1].services
        context['bio'] = context['imagerprofile_list'][1].bio
        context['phone'] = context['imagerprofile_list'][1].phone_number
        context['photo_style'] = context['imagerprofile_list'][1].photo_style
        return context




#View from Chris
# class ProfileView(ListView):
#     """Privet profile page."""

#     template_name = "imagersite/profile.html"
#     model = ImagerProfile

#     def get_context_data(self, **kwargs):
#         """Setup context for page."""
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         # import pdb; pdb.set_trace()
#         context['phone'] = context['imagerprofile_list'][1].phone_number
#         context['pub_pics'] = (ImagerPhoto.objects
#                                .filter(user=self.request.user)
#                                .filter(published='PB')).count()
#         context['pub_albums'] = (ImagerAlbum.objects
#                                  .filter(user=self.request.user)
#                                  .filter(published='PB')).count()
#         context['prv_pics'] = (ImagerPhoto.objects
#                                .filter(user=self.request.user)
#                                .filter(published='PV')).count()
#         context['prv_albums'] = (ImagerAlbum.objects
#                                  .filter(user=self.request.user)
#                                  .filter(published='PV')).count()
#         context['profile'] = context['view'].request.user.imagerprofile
#         context['camera'] = context['profile'].get_camera_type_display()
#         context['photostyle'] = context['profile'].get_photo_style_display()
#         context['location'] = (context['profile'].city + ', ' + context['profile'].state)
#         return context



class ProfileEditView(UpdateView):
    """View for editing the users profile."""

    model = User
    template_name = 'imagersite/edit.html'
    success_url = reverse_lazy('profile')
    fields = []

    def get_object(self):
        """Return the user."""
        return self.request.user

    def get_context_data(self, **kwargs):
        """Set the form."""
        context = super(ProfileEditView, self).get_context_data(**kwargs)
        context['form'] = ProfileForm()


    def post(self, request, *args, **kwargs):
        """Set the new info."""
        self.object = self.get_object()
        user = request.user
        info = request.POST
        # import pdb; pdb.set_trace()
        if 'phonenumber' in info.keys():
            if 'phonenumber' in info.keys():
                user.profile.phone_number = info['phonenumber']
            else:
                user.profile.phone_number = user.profile.phone_number

        # if info['username'] and info['email']:
        #     if info['username']:
        #         user.username = info['username']
        #     else:
        #         user.username = user.username
        #     if info['email']:
        #         user.email = info['email']
        #     else:
        #         user.email = user.email
        #     if 'first_name' in info.keys():
        #         user.first_name = info['first_name']
        #     else:
        #         user.first_name = user.first_name
        #     if 'last_name' in info.keys():
        #         user.last_name = info['last_name']
        #     else:
        #         user.last_name = user.last_name
        #     if 'photo_style' in info.keys():
        #         user.imagerprofile.photo_style = info['photo_style']
        #     else:
        #         user.imagerprofile.photo_style = user.imagerprofile.photo_style
        #     if 'camera_type' in info.keys():
        #         user.imagerprofile.camera_type = info['camera_type']
        #     else:
        #         user.imagerprofile.camera_type = user.imagerprofile.camera_type
        #     if 'job' in info.keys():
        #         user.imagerprofile.job = info['job']
        #     else:
        #         user.imagerprofile.job = user.imagerprofile.job
        #     if 'website' in info.keys():
        #         user.imagerprofile.website = info['website']
        #     else:
        #         user.imagerprofile.website = user.imagerprofile.website
            user.save()
            user.profile.save()

            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(**kwargs))
