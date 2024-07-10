# A sample websocket server for displaying notifications

## How to run

1. Start redis for the channel layer:
```
    docker run -d --name redis -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```
2. Start RabbitMQ:
```
    docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```
3. Install requirements
```
    pip3 install -r requirements.txt
```
4. Start frontend
```
    python3 manage.py tailwind install
```
5. Start websocket server
Please, run this in a different terminal or tab.
```
    python3 manage.py runserver
```
6. Run the rabbitmq consumer
Please, run this in a different terminal or tab.
```
    python3 manage.py rabbitmq_consumer
```
7. Run the test script
```
    python3 test.py
```
Now head to the localhost:8000/notifications to see the result.