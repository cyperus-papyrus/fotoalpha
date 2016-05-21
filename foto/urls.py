# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from fotoalpha import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^foto/(?P<url>[\w+-_]+)/$', views.foto, name='foto'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^category/(?P<category>[0-9]+)/$', views.categories, name='categories'),
    url(r'^contact/', views.contact, name='contact'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'foto.views.show_404'
handler404 = 'foto.views.show_404'
