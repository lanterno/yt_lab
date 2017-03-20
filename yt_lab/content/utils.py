import os
from datetime import timedelta
from apiclient.discovery import build

from .models import Video

yt = build('youtube', 'v3', developerKey=os.environ.get("GOOGLE_API_KEY"))


def prase_youtube_duration(duration):
    '''
    Parses a youtube duration string that looks like this "PT1H57M31"
    and returns a python timedelta object
    '''
    duration = duration[2:]  # remove the first two chars "PT"
    time = []
    # the following for loop should result in a list of three integers
    # [Hours, Minutes, Seconds]
    for time_part in ["H", "M", "S"]:
        if len(duration.split(time_part)) == 2:
            time.append(int(duration.split(time_part)[0]))
            duration = duration.split(time_part)[1]
        else:
            time.append(0)
    return timedelta(hours=time[0], minutes=time[1], seconds=time[2])


def update_source_info(source):
    '''
    Input: a Source object
    function: get title from youtube API
    '''
    # get name or title
    if source.typ == source.CHANNEL:
        response = yt.channels().list(part="snippet", fields="items(snippet(title))", id=source.id).execute()
        source.title = response['items'][0]['snippet']['title']
    elif source.typ == source.PLAYLIST:
        response = yt.playlists().list(part="snippet", fields="items(snippet(title))", id=source.id).execute()
        source.title = response['items'][0]['snippet']['title']
    source.save()


def update_source_videos(source):
    '''
    input: a Source object
    function: get_or_update all related objects to the source provided
    '''
    if source.typ == source.PLAYLIST:
        playlist_id = source.id
    else:
        # every channel has a standard playlist called uploads that has all of it's videos
        # ref: https://developers.google.com/youtube/v3/guides/implementation/videos
        response = yt.channels().list(
            part="contentDetails",
            id=source.id,
            fields="items(contentDetails)"
        ).execute()
        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # get all video_ids in the playlist
    videos = yt.playlistItems().list(
        part="contentDetails", playlistId=playlist_id,
        fields="items(contentDetails(videoId))", maxResults=50
    ).execute()
    video_ids = [video['contentDetails']['videoId'] for video in videos['items']]
    # retrieve all needed info about those videos from the videos API
    videos = yt.videos().list(
        part="snippet,statistics,contentDetails", id=",".join(video_ids),
        fields="items(id,snippet(title,thumbnails(default(url),maxres(url))),\
                statistics(viewCount),contentDetails(duration))"
    ).execute()
    for video in videos['items']:
        Video.objects.get_or_create(
            source=source,
            id=video['id'],
            url='https://www.youtube.com/watch?v={}'.format(video['id']),
            title=video['snippet']['title'],
            duration=prase_youtube_duration(video['contentDetails']['duration']),
            views_count=int(video['statistics']['viewCount']),
            thumbnail=video['snippet']['thumbnails']['default']['url'],
            image=video['snippet']['thumbnails']['maxres']['url']
        )
