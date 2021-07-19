from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.exceptions import StopConsumer


class WSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add("coins", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("coins", self.channel_name)
        raise StopConsumer()

    async def send_new_data(self, event):
        text_message = event['text'] # receive from celery (tasks.py)
        await self.send(json.dumps(text_message)) # send to client
