from kafka import KafkaProducer
import json

TOPIC_NAME = 'interview_ready_applicants'
BROKER = 'localhost:9092'

def produce_messages():
    producer = KafkaProducer(
        bootstrap_servers=BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    try:
        for i in range(10):
            message = {"message_number": i, "content": f"Hola mundo {i}"}
            producer.send(TOPIC_NAME, value=message)
            print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error producing messages: {e}")
    finally:
        producer.close()

if __name__ == '__main__':
    produce_messages()

