from celery import shared_task
from celery.utils.log import get_task_logger
from googleapiclient.discovery import build
import os


logger = get_task_logger(__name__)
youtube = build('youtube', 'v3', developerKey=os.environ.get("YOUTUBE_API_KEY"))


@shared_task
def get_new_videos():
    # fetch data from youtube
    request = youtube.search().list(
        part= 'id, snippet',
        maxResults=10,
        publishedAfter="2020-01-01T00:00:00Z",
        q="fampay",
        type="video"
    )
    response = request.execute()        

    logger.info(response)
