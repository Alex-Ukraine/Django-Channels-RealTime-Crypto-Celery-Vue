TASK:
> You need to store in DB currency exchange BTC-USD with time interval 35sec.
>
> Service needs to has web-interface - site where you can currency values and average values for 2 last minutes.
>
> User can enter a new pair of thr currencies,  and it will be added to list for receiving.
>
> Currency exchange is available on many sites - for instance https://ru.cryptonator.com/api/
>
> It's preferable to use Django.
>
> push on GitHub.
>
> Front-end for your discretion
>
> Docker will be a plus but not necessary 
>
> For request with interval you can use Celery or for your discretion.

***************************************************************

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
   (ccymc IS cryptocurrency-monetary currency)
>
> celery -A ccymc worker -l info
> 
5. Start celery beat
> celery -A ccymc beat -l info