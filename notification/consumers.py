import json

from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    group_name = "document_status_group"
    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard( self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name, {
                "type": "notification.message",
                "message": text_data_json
            }
        )

    async def notification_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))