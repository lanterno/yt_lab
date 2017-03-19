from apiclient.discovery import build
import os

yt = build('youtube', 'v3', developerKey=os.environ.get("GOOGLE_API_KEY"))


def update_source_info(source):
    '''
    Input: a Source object
    function: get title from youtube API
    '''
    # get name or title
    if source.typ == source.CHANNEL:
        response = yt.channels().list(part="snippet", fields="items(snippet(title))", id=source.youtube_id).execute()
        source.title = response['items'][0]['snippet']['title']
    elif source.typ == source.PLAYLIST:
        response = yt.playlists().list(part="snippet", fields="items(snippet(title))", id=source.youtube_id).execute()
        source.title = response['items'][0]['snippet']['title']
    source.save()


def update_source_videos(source):
    '''
    input: a Source object
    function: get_or_update all related objects to the source provided
    '''
    if source.typ == source.PLAYLIST:
        pass
    elif source.typ == source.CHANNEL:
        pass
