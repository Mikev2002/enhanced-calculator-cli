import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(key, default=None, var_type=str):
    value = os.getenv(key, default)
    try:
        return var_type(value)
    except Exception:
        return default

# Access config values like:
LOG_DIR = get_env_variable("CALCULATOR_LOG_DIR", "logs")
HISTORY_DIR = get_env_variable("CALCULATOR_HISTORY_DIR", "history")
MAX_HISTORY_SIZE = get_env_variable("CALCULATOR_MAX_HISTORY_SIZE", 100, int)
AUTO_SAVE = get_env_variable("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
PRECISION = get_env_variable("CALCULATOR_PRECISION", 2, int)
MAX_INPUT_VALUE = get_env_variable("CALCULATOR_MAX_INPUT_VALUE", 1000000, int)
DEFAULT_ENCODING = get_env_variable("CALCULATOR_DEFAULT_ENCODING", "utf-8")
