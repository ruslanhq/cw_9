from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializer import CommentSerializer, LikeSerializer
from webapp.models import Comment, Like


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author= self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        like = self.get_object()
        if like.like != True:
            like.like = True
            like.save()
            return Response({'id': like.photo.pk, 'like': like.like})

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        like = self.get_object()
        if like.like == True:
            like.like = False
            like.save()
            return Response({'id': like.photo.pk, 'like': like.like})
