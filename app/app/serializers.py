from rest_framework.serializers import ModelSerializer

from app.models import Video, Channel


class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        read_only = True
        fields = "__all__"


class VideoDetailSerializer(ModelSerializer):
    class Meta:
        model = Video
        read_only = True
        exclude = ['id', 'youtube_id']
        depth = 1


class VideoListSerializer(ModelSerializer):
    class Meta:
        model = Video
        read_only=True
        exclude = ['youtube_id', 'description', "channel"]
