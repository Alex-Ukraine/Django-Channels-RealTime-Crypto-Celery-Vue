web: set DISABLE_COLLECTSTATIC=1
web: python manage.py migrate
web: python manage.py collectstatic --noinput
web: unset DISABLE_COLLECTSTATIC
# web: gunicorn ccymc.wsgi
web: celery -A ccymc worker -l info
worker: celery -A ccymc beat -l info
