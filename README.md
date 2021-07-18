1. create dir and clone git repo

2. Issues with virtualenv:
> pip install virtualenv
> 
> virtualenv venv
> 
> source venv/bin/activate
> 
> pip install -r requirements.txt
> 
3. Then start runserver:
> python3 manage.py runserver
>
4. Start celery worker
> celery -A setari worker -l info)
> 
5. Start celery beat
> celery -A setari beat -l info