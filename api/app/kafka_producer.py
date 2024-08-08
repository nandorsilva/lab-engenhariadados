from confluent_kafka import Producer
from .configs import settings


kafka_conf = {
    'bootstrap.servers': settings.BOOSTRAP_SERVER
}

producer = Producer(**kafka_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_message(topic, value):
    producer.produce(topic, value=value, callback=delivery_report)
    producer.flush()