from __future__ import absolute_import, unicode_literals

import datetime
import time

from celery.decorators import task
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Coin, Pair

channel_layer = get_channel_layer()


@task(name="get_the_data")
def get_joke():
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    part_url = 'https://api.cryptonator.com/api/ticker/'
    pairs = []
    for p in Pair.objects.all():
        pairs.append(p.name)
    coins = list()
    for x in pairs:
        url = part_url+x
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            response = response.json()

            obj, created = Coin.objects.get_or_create(base=response["ticker"]["base"],
                                                      target=response["ticker"]["target"],
                                                      timestamp=response["timestamp"],
                                                      price=response["ticker"]["price"])

            print(obj, created)

            searched = Coin.objects.filter(base=response["ticker"]["base"], target=response["ticker"]["target"],
                                           timestamp__gt=(int(datetime.datetime.now().timestamp())-120))
            avg = obj.price
            print(searched)
            if searched.count():
                sum=0
                for row in searched:
                    sum += row.price

                avg = sum/searched.count()
                print(sum, avg)

            coins.append({'base': obj.base, 'target': obj.target,
                          'timestamp': time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(obj.timestamp)),
                          'price': obj.price, 'avg': avg})
        else:
            to_delete = Pair.objects.get(name=x)
            to_delete.delete()

    async_to_sync(channel_layer.group_send)('coins', {'type': 'send_new_data', 'text': coins})
