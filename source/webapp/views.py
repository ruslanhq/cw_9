from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Photo


class IndexView(ListView):
    context_object_name = 'photos'
    template_name = 'index.html'
    model = Photo
    ordering = '-created_at'
