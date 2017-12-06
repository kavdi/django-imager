from django.conf.urls import url
from imager_images.views import LibraryView, AlbumView, AlbumDetailView, PhotoView, PhotoDetailView


urlpatterns = [
    url(r'library/$', LibraryView.as_view(), name='library'),
    url(r'photos/$', PhotoView.as_view(), name='all_photos'),
    url(r'photos/(?P<pk>\d+)$', PhotoDetailView.as_view(), name='detail_photo'),
    url(r'albums/$', AlbumView.as_view(), name='all_albums'),
    url(r'albums/(?P<pk>\d+)$', AlbumDetailView.as_view(), name='detail_album')
]
