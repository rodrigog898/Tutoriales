from kafka import KafkaConsumer
import json

TOPIC_NAME = 'interview_ready_applicants'
BROKER = 'localhost:9092'

def consume_messages():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BROKER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    try:
        print(f"Consuming messages from topic: {TOPIC_NAME}")
        for message in consumer:
            print(f"Message received: {message.value}")
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_messages()

