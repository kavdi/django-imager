"""imagersite URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from imager_profile.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^/', include('registration.backends.hmac.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls'))
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL
    )
