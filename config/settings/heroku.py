from .common import *  # noqa

import dj_database_url


DEBUG = True

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = '@#$RSDFDSfsfdg#$wrwer234234234DSFDSFDSF%#$%@#$@$DFGDFG'


# This ensures that Django will be able to detect a secure connection properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WHITENOISE_MIDDLEWARE = ('whitenoise.middleware.WhiteNoiseMiddleware', )
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['yt-lab.herokuapp.com'])

INSTALLED_APPS += ('gunicorn', )


# Static Assets
# ------------------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES['default'] = dj_database_url.config()

# CELERY SETTINGS
# ------------------------------------------------------------------------------
BROKER_URL = env('REDIS_URL')
CELERY_RESULT_BACKEND = BROKER_URL
