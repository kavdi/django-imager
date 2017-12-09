from imager_images.models import Album, Photo
from imager_images.forms import AlbumForm, PhotoForm
from django.views.generic import DetailView, ListView, CreateView
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


class AlbumDetailView(ListView):
    """Set up a detail ablum view."""
    template_name = 'imagersite/album_detail.html'
    model = Album

    def get_context_data(self):
        """Get the album and photos."""
        album = Album.objects.get(id=self.kwargs['pk'])
        photos = album.photos.all()
        return {'album': album, 'photos': photos}


class PhotoDetailView(DetailView):
    """Set up a detail photo view."""
    template_name = 'imagersite/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        """Get photo by id."""
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        context['photo'] = Photo.objects.get(id=self.kwargs['pk'])
        return context


class AddAlbumView(CreateView):
    """Create a new album."""
    template_name = 'imager_images/add_album.html'
    model = Album
    success_url = reverse_lazy('library')
    form_class = AlbumForm

    def form_valid(self, form):
        """."""
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class AddPhotoView(CreateView):
    """Create a new photo."""
    template_name = 'imager_images/add_photo.html'
    model = Photo
    success_url = reverse_lazy('library')
    form_class = PhotoForm

    def form_valid(self, form):
        """Validate the user is allowed to upload photo."""
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)
