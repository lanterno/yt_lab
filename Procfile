web: gunicorn config.wsgi:application --timeout 60 --keep-alive 5 --log-level debug
worker: celery worker --app=yt_lab.taskapp --loglevel=info
