from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Photo


class IndexView(ListView):
    context_object_name = 'photos'
    template_name = 'index.html'
    model = Photo
    ordering = '-created_at'


class PhotoView(DetailView):
    pk_url_kwarg = 'pk'
    model = Photo
    template_name = 'photo.html'
    context_object_name = 'photo'
