import pika

connection_params = pika.ConnectionParameters(host='localhost',port=5672,virtual_host='krolik', credentials=pika.PlainCredentials('login','pass')),
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

exchange_name = 'test_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

queue_name = 'test_queue'
channel.queue_declare(queue=queue_name, arguments={'x-message-ttl': 3600000})

channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='')

sample_messages = ['max', 'bob', 'lll']

for message in sample_messages:
    channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
    print(f" [x] Sent '{message}' to {exchange_name}")

connection.close()
