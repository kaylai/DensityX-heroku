from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
    url(r'^$', views.simple_upload, name='home'),
    url(r'^readthedocs', views.readthedocs, name='readthedocs'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
