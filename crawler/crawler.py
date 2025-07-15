import time
import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'crawler.out.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Crawler started.")

try:
    while True:
        logging.info("Dummy crawling activity running...")
        time.sleep(10)
except KeyboardInterrupt:
    logging.info("Crawler stopped by KeyboardInterrupt.")
