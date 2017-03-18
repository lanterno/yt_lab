from coreapi import Document, Link, Field


BASE_URL = '/api/v1/'
BASE_AUTH_URL = BASE_URL + 'auth/'
BASE_ANALYTICS_URL = BASE_URL + 'analytics/'

SCHEMA = Document(
    title='YouTube Lab API',
    content={
    }
)
