from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin

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


class PhotoCreate(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoForm
    permission_denied_message = 'Доступ запрещен'

    def get_success_url(self):
        return reverse('webapp:photo', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PhotoUpdate(UserPassesTestMixin, UpdateView):
    form_class = PhotoForm
    template_name = 'update.html'
    model = Photo
    context_object_name = 'photo'
    # permission_required = 'webapp.change_photo'
    # permission_denied_message = 'Запрещено'

    # def test_func(self):
    #     photo = self.get_object()
    #     if self.request.user == photo.author or self.request.user.is_superuser \
    #            or self.request.user.has_perm('webapp.change_photo'):
    #         return True
    #     return False

    def test_func(self):
        photo = Photo.objects.filter(author__username=self.request.user, pk=self.kwargs['pk'])
        if photo or self.request.user.has_perm('webapp.change_photo'):
            return True

    def get_success_url(self):
        return reverse('webapp:photo', kwargs={'pk': self.object.pk})


class PhotoDelete(UserPassesTestMixin, DeleteView):
    template_name = 'delete.html'
    model = Photo
    context_object_name = 'photo'

    def test_func(self):
        photo = Photo.objects.filter(author__username=self.request.user, pk=self.kwargs['pk'])
        if photo or self.request.user.has_perm('webapp.delete_photo'):
            return True

    def get_success_url(self):
        return reverse_lazy('webapp:index')
