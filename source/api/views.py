from django.shortcuts import render
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
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


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]
