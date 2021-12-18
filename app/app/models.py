from django.db import models
import uuid


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishing_date = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
