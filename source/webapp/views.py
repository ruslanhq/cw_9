from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PhotoForm
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


class PhotoCreate(CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('webapp:photo', kwargs={'pk': self.object.pk})
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.author = self.request.user
    #     return
