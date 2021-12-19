from celery import shared_task
from celery.utils.log import get_task_logger
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

from app.models import Video, Channel


logger = get_task_logger(__name__)
YOUTUBE_API_KEYS = os.environ.get("YOUTUBE_API_KEYS").split(" ")
key_val = 0
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEYS[0])


def shift_api_key():
    global key_val
    len_keys = len(YOUTUBE_API_KEYS)

    if len_keys == 1:
        logger.info("Only 1 API key was supplied and it's quota is exhausted!!")
        return
    
    if key_val < len_keys - 1:
        key_val = key_val + 1
    elif key_val == len_keys - 1:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEYS[0])
    
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEYS[key_val])
    logger.info("API KEY SHIFTED.")
    

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
    try:
        response = request.execute()
    except HttpError as e:
        logger.info(f'Error response status code : {e.status_code}, reason : {e.error_details} {YOUTUBE_API_KEYS[key_val]}')
        shift_api_key()
        return
    count = 0

    for data in response['items']:
        if not Channel.objects.filter(channel_id=data['snippet']['channelId']).exists():
            Channel.objects.create(
                channel_id=data['snippet']['channelId'],
                channel_url="https://www.youtube.com/channel/" + data['snippet']['channelId'],
                channel_title=data['snippet']['channelTitle'],
            )
        if not Video.objects.filter(youtube_id=data['id']['videoId']).exists():
            channel = Channel.objects.get(channel_id=data['snippet']['channelId'])
            Video.objects.create(
                youtube_id=data['id']['videoId'],
                title=data['snippet']['title'],
                description=data['snippet']['description'],
                publishing_date=data['snippet']['publishedAt'],
                thumbnail_url=data['snippet']['thumbnails']['medium']['url'],
                url="https://www.youtube.com/watch?v=" + data['id']['videoId'],
                channel=channel,
                live_broadcast=data['snippet']['liveBroadcastContent'],
            )
            count = count + 1

    logger.info(f"{count} objects created.")
