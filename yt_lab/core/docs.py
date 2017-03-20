from coreapi import Document, Link, Field


CONTENT_BASE_URL = '/api/v1/content/'

SCHEMA = Document(
    title='YouTube Lab API',
    content={
        'Content Source': {
            'list_all_sources': Link(
                url=CONTENT_BASE_URL + 'sources/',
                action='get',
                description="""
                    List all Content sources in the database

                    Returns a list with all playlists and channels in the database
                """,
            ),
            'add_new_source': Link(
                url=CONTENT_BASE_URL + 'sources/',
                action='post',
                description="""
                    Add a new content source ex. playlist

                    Provide a url to the playlist or channel you want to Crawl
                """,
                fields=[
                    Field(
                        name='url',
                        required=True,
                        location='formData',
                    )
                ]
            ),
            'remove_source': Link(
                url=CONTENT_BASE_URL + 'sources/{pk}/',
                action='delete',
                description="""
                    Remove an existing source from the database

                    Provide pk to the playlist or channel you want to remove
                """,
                fields=[
                    Field(
                        name='pk',
                        required=True,
                        location='path',
                    )
                ]
            ),
        },
        'Videos': {
            'list_videos_from_source': Link(
                url=CONTENT_BASE_URL + 'sources/{source_id}/videos',
                action='get',
                description="""
                    Lists all the videos related to a certain source

                    Enter the id of the playlist of channel you want to check.
                """,
                fields=[
                    Field(
                        name='source_id',
                        required=True,
                        location='path'
                    )
                ]
            ),
            'download_video': Link(
                url=CONTENT_BASE_URL + 'sources/{source_id}/videos/{video_id}/download/',
                action='get',
                description="""
                    Get direct download link for youtube video
                """,
                fields=[
                    Field(
                        name='source_id',
                        required=True,
                        location='path'
                    ),
                    Field(
                        name='video_id',
                        required=True,
                        location='path'
                    )
                ]
            ),
        }
    }
)
