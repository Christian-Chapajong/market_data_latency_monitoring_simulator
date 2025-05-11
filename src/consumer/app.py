import redis
import time
import logging
from prometheus_client import start_http_server, Counter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

messages_processed = Counter("messages_processed_total", "Total messages processed")
start_http_server(8000)  # expose Prometheus endpoint on container port

def handle_msg(msg):
    if msg["type"] == "message":
        logger.info(f"Received message: {msg['data'].decode()}")
    else:
        logger.info(f"Other message: {msg}")
    
    messages_processed.inc()

def main():
    try:
        r = redis.Redis(host="redis", port=6379)
        pubsub = r.pubsub()
        pubsub.subscribe("market-feed")

        logger.info("Subscribed to 'market-feed'. Waiting for messages...")

        for msg in pubsub.listen():
            handle_msg(msg)
    except Exception as e:
        logger.error(f"Error in consumer: {e}")
        time.sleep(5)

if __name__ == "__main__":
    main()