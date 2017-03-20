YouTube Lab
===========

YouTube Lab is a service that simply takes in a link for a playlist or a channel and returns a list of available videos in that channel or playlist. The list is periodically updated.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Installation Steps
--------------------

.. code-block:: bash

    pip install -r requirements/local.txt
    sudo apt-get install redis-server
    python manage.py migrate


Run Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd yt_lab
    celery -A yt_lab.taskapp worker -l info
    celery -A yt_lab.taskapp beat

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Start it out
^^^^^^^^^^^^^

To run the server, simply run the following command
```python manage.py runserver```

then navigate using your browser to the following location localhost:8000/api/v1/docs
and in the Content Source tab, start by adding a new playlist or a channel.
try adding a link that isn't a youtube link and see what happens.
after that, you can try and list all the sources to see if the sources are updated with right titles.

After a couple of seconds from creating the source, you can checkout the videos that we have retrieved from that
source by navigating to the videos tab and providing the id of any resource you created.

here's some technical points I considered while building this:

* Used the same youtube IDs in our own tables
* Prevented duplicate sources(a playlist, channel, or a user is considered a source or a content source)
* Used Swagger to document the APIs and for easier testing by frontend devs and users
* One other big thing is the use or REGEX to handle the inputted URL and allow as many patterns as possible:
    * URL must be a youtube link
    * URL doesn't need to be in a very specific format, so any inner page in the channel page would work
    * users and channels both are considered channels and the system handles and understands both of them
* Django signals is used to facilitate and divide different concerns
* Celery is used to handle ALL the Youtube crawling
* celery beat updates the videos every 3 hours
* Finally, Heroku settings and Docker configurations are available for easier deployment on different platforms. 

Current limitations and future improvements:
* I didn't save the images into local storage because that would cause a big hassle with the deployment and I wanted to show you the project deployed.
* currently the system only pulls the first 50 videos from any source
* The project has no tests currently and therefore could fail with any upgrade(highest priority)

Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


