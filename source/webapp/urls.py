from django.urls import path

from webapp.views import IndexView, PhotoView, PhotoCreate

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo'),
    path('photo/create/', PhotoCreate.as_view(), name='create')
]