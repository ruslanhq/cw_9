from rest_framework.serializers import ModelSerializer

from webapp.models import Comment, Like


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created_at']


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'photo', 'author', 'like']
