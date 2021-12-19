from django.db import models
import uuid


class Channel(models.Model):
    channel_url = models.URLField()
    channel_id = models.CharField(max_length=30, unique=True)
    channel_title = models.CharField(max_length=255)

    def __str__(self):
        return self.channel_title


class Video(models.Model):
    LIVE_BRODCAST_CHOICES = (
        ("upcoming", "upcoming"),
        ("live", "live"),
        ("none", "none"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publishing_date = models.DateTimeField()
    thumbnail_url = models.URLField()
    youtube_id = models.CharField(max_length=30, unique=True)
    url = models.URLField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    live_broadcast = models.CharField(max_length=10, choices=LIVE_BRODCAST_CHOICES)

    def __str__(self):
        return self.title
