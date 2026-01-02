import logging
import os
from datetime import datetime

# ===============================
# Base directory
# ===============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    f"ml_app_{datetime.now().strftime('%Y_%m_%d')}.log"
)

# ===============================
# Create formatter
# ===============================
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)

# ===============================
# Create handlers
# ===============================
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# ===============================
# Root logger config
# ===============================
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Avoid duplicate handlers
if not root_logger.handlers:
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)


def get_logger(name: str):
    return logging.getLogger(name)
