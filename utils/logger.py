import logging
import sys

__all__ = [
    'logger',
]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] " + 
    "[%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger()

