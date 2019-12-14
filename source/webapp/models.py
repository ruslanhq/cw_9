from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(upload_to='user_pics', verbose_name='Картинка')
    sign = models.CharField(max_length=100, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    like = models.IntegerField(default=0, verbose_name='Лайки')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='a_post')

    def __str__(self):
        return self.sign


class Comment(models.Model):
    text = models.TextField(max_length=50, verbose_name='Комментарий')
    photo = models.ForeignKey('webapp.Photo', related_name='comments', on_delete=models.CASCADE, verbose_name='Фото')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='a_comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text
