from django import forms
from imager_images.models import Album, Photo


class AlbumForm(forms.ModelForm):
    """From for album create view."""

    class Meta:
        """Meta for ablum form."""
        model = Album
        exclude = ['date_uploaded', 'date_modified', 'date_published', 'user']


class PhotoForm(forms.ModelForm):
    """From for photo create view."""

    class Meta:
        model = Photo
        exclude = ['date_created', 'date_modified', 'date_published', 'user']
