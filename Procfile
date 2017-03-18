web: gunicorn config.wsgi:application
worker: celery worker --app=yt_lab.taskapp --loglevel=info
