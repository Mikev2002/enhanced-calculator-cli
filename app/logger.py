import logging
import os
from app.calculator_config import LOG_DIR

LOG_FILE = os.path.join(LOG_DIR, "calculator.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name="CalculatorLogger"):
    return logging.getLogger(name)
