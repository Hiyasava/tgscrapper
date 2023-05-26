import pika
import json 


class WriteToRabbit():
    def POST(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='POST', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='POST',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()

    
    def DELETE(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='DELETE', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='DELETE',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()


    def EDIT(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='EDIT', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='EDIT',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()


    def FORWARD(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='FORWARD', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='FORWARD',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()


    def MEDIA(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='MEDIA', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='MEDIA',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()


    def REPLY(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='REPLY', durable=True)

        channel.basic_publish(exchange='',
                      routing_key='REPLY',
                      body=json.dumps(message, ensure_ascii=False, default=str),
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
        connection.close()