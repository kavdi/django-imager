from django.conf.urls import url
from imager_profile.views import ProfileView, OtherProfileView, ProfileEditView


urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='my_profile'),
    url(r'^(?P<slug>\w+)/$', OtherProfileView.as_view(), name='profile'),
    url(r'edit/$', ProfileEditView.as_view(), name='profile_edit'),
]
