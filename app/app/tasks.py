from celery import shared_task
from celery.utils.log import get_task_logger
from googleapiclient.discovery import build
import os

from app.models import Video


logger = get_task_logger(__name__)
youtube = build('youtube', 'v3', developerKey=os.environ.get("YOUTUBE_API_KEY"))


@shared_task
def get_new_videos():
    # fetch data from youtube
    request = youtube.search().list(
        part= 'id, snippet',
        order="date",
        maxResults=10,
        publishedAfter="2020-01-01T00:00:00Z",
        q="fampay",
        type="video",
    )
    response = request.execute()
    count = 0

    for data in response['items']:
        if not Video.objects.filter(youtube_id=data['id']['videoId']).exists():
            Video.objects.create(
                youtube_id=data['id']['videoId'],
                title=data['snippet']['title'],
                description=data['snippet']['description'],
                publishing_date=data['snippet']['publishedAt'],
                thumbnail_url=data['snippet']['thumbnails']['medium']['url'],
                url="https://www.youtube.com/watch?v=" + data['id']['videoId'],
            )
            count = count + 1

    logger.info(f"{count} objects created.")
