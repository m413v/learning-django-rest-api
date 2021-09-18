from rest_framework import serializers

from posts.models import Post
from users.serializers import UserSerializer


class PostRetrieveSerializer(serializers.ModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author'
        )
