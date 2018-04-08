from rest_framework import serializers
from core.models import Reporter, Post


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ['id','name', 'email', 'password', 'avatar', 'avatar_url']
        read_only_fields = ['avatar_url']


class PostSerializer(serializers.ModelSerializer):

    reporter_avatar = serializers.CharField(read_only=True, source="reporter.avatar_url")
    reporter_name = serializers.CharField(read_only=True, source="reporter.name")

    class Meta:
        model = Post
        fields = ['id','title', 'body', 'picture', 'video',
        'like', 'rating', 'reporter', 'picture_url', 'video_url', 'reporter_name', 'reporter_avatar', 'date_formated', 'star_color']
        read_only_fields = ['picture_url', 'video_url', 'date_formated']
