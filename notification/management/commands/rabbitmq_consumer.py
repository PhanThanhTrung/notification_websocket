import pika
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run RabbitMQ consumer'

    def handle(self, *args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='documents')

        def callback(ch, method, properties, body):
            message = json.loads(body)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "document_status_group",
                {
                    "type": "notification.message",
                    "message": message,
                }
            )

        channel.basic_consume(queue='documents', on_message_callback=callback, auto_ack=True)

        self.stdout.write(self.style.SUCCESS('Started RabbitMQ consumer...'))
        channel.start_consuming()
