import json
from channels.testing import WebsocketCommunicator
from django.test import TransactionTestCase
from notification.consumers import NotificationConsumer

class WebSocketConsumerTestCase(TransactionTestCase):
    async def test_receive_message(self):
        communicator = WebsocketCommunicator(NotificationConsumer.as_asgi(), "/ws/notifications/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        payload = {"document_id": 1, "status": "completed", "timestamp": 1626424793.123456}
        await communicator.send_json_to({
            "type": "notification.message",
            "message": payload
        })

        response = await communicator.receive_json_from()
        response = response['message']
        self.assertEqual(response, {
            'message': payload
        })

        await communicator.disconnect()