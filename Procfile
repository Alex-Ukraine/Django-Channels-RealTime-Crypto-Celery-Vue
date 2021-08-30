web: python manage.py collectstatic --noinput
web: gunicorn ccymc.wsgi
worker: python manage.py celery worker --loglevel=info
celery_beat: python manage.py celery beat --loglevel=info