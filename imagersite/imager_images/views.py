from imager_images.models import Album, Photo
from django.views.generic import DetailView, TemplateView, ListView
from django.urls import reverse_lazy


class LibraryView(ListView):
    """Set up list view for all albums and pictures."""
    template_name = 'imagersite/library.html'
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        """Get all the photos and albums."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        user = self.request.user
        context['photos'] = user.photos.all()
        context['albums'] = user.albums.all()
        return context


class AlbumView(ListView):
    """Set up list view for albums."""
    template_name = 'imagersite/album.html'
    model = Album
    context_object_name = 'albums'

    def get_context_data(self, **kwargs):
        """Get all public Albums from app."""
        context = super(AlbumView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(published='Public').all()
        return context


class PhotoView(ListView):
    """Set up list view for photos."""
    template_name = 'imagersite/photo_view.html'
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        """Get all public Albums from app."""
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(published='Public').all()
        return context


class AlbumDetailView(DetailView):
    """Set up a detail ablum view."""
    template_name = 'imagersite/album_detail.html'
    model = Album
    slug_field = 'title'
    context_object_name = 'album'


class PhotoDetailView(DetailView):
    """Set up a detail photo view."""
    template_name = 'imagersite/photo_detail.html'
    model = Photo
    slug_field = 'title'
    context_object_name = 'photo'
