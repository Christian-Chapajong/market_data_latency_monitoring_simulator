import redis
import time
import json
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def generate_fake_quote():
    return {
        "instrument": "BTC-USD",
        "bid": round(random.uniform(29500, 30500), 2),
        "ask": round(random.uniform(30500, 31500), 2),
        "timestamp": time.time()
    }

def main():
    try:
        r = redis.Redis(host="redis", port=6379)
        logger.info("Connected to Redis. Publishing messages...")

        while True:
            quote = generate_fake_quote()
            message = json.dumps(quote)
            r.publish("market-feed", message)
            logger.info(f"Published: {message}")
            time.sleep(1)  # adjust to control frequency
    except Exception as e:
        logger.error(f"Simulator error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    main()
