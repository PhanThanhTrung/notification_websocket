import pika
import json
import random
import time

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='documents')

    while True:
        document_id = random.randint(1, 1000)
        status = random.choice(['processing', 'completed', 'failed'])
        payload = {
            'text': f"Document: {document_id} | status: {status} | timestamp{time.time()}"
        }

        channel.basic_publish(
            exchange='',
            routing_key='documents',
            body=json.dumps(payload)
        )

        print(f" [x] Sent {payload}")
        time.sleep(random.uniform(1, 5))  # Sleep for a random time between 1 and 5 seconds

    connection.close()

if __name__ == "__main__":
    publish_message()
