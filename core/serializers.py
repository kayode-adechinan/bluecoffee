from rest_framework import serializers
from core.models import Reporter, Post,FileHandler


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ['name', 'email', 'password', 'avatar', 'avatar_url']
        read_only_fields = ['avatar_url']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'picture', 'video',
        'like', 'rating', 'reporter', 'picture_url', 'video_url']
        read_only_fields = ['picture_url', 'video_url']


class ApiResponseSerializer(serializers.Serializer):
    response = serializers.DictField()
    status = serializers.CharField()

class FileHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileHandler
        fields = ['picture', 'video']
