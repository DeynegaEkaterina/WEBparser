import pika
from main import get_product_info, get_product_links
import threading
from data import nav


def callback(ch, method, properties, body):
    link = body.decode('utf-8')
    print(f"[CONSUMER INFO] Получил сообщение {link}")
    get_product_info(link)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='new_queue', durable=True)
    print("[CONSUMER INFO] Жду ссылку на товар")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='new_queue', on_message_callback=callback, auto_ack=False)
    channel.start_consuming()


def send(link):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='new_queue', durable=True)
    message = link
    channel.basic_publish(
        exchange='',
        routing_key='new_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    connection.close()


def main():
    for category in nav:
        links = get_product_links(category)
        for link in links:
            send(link)


if __name__ == '__main__':
    producer = threading.Thread(target=main).start()
    consumer = threading.Thread(target=receive).start()
