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

                    Provide a url to the playlist of channel you want to Crawl
                """,
                fields=[
                    Field(
                        name='url',
                        required=True,
                        location='formData',
                    )
                ]
            ),
        },
        'Videos': {
            'list_videos_from_source': Link(
                url=CONTENT_BASE_URL + 'sources/{pk}/videos',
                action='get',
                description="""
                    Lists all the videos related to a certain source

                    Enter the id of the playlist of channel you want to check.
                """,
                fields=[
                    Field(
                        name='pk',
                        required=True,
                        location='path'
                    )
                ]
            ),
        }
    }
)
