import os
import pandas as pd
from app.calculator_config import HISTORY_DIR, AUTO_SAVE
from app.logger import get_logger

logger = get_logger()

class Observer:
    def update(self, calculation):
        pass

class LoggingObserver(Observer):
    def update(self, calculation):
        logger.info(
            f"Operation: {calculation.operation_name}, A: {calculation.a}, B: {calculation.b}, Result: {calculation.result}"
        )

class AutoSaveObserver(Observer):
    def __init__(self, calculator):
        self.calculator = calculator
        os.makedirs(HISTORY_DIR, exist_ok=True)

    def update(self, _):
        if not AUTO_SAVE:
            return
        df = pd.DataFrame([c.to_dict() for c in self.calculator.get_history()])
        file_path = os.path.join(HISTORY_DIR, "calc_history.csv")
        df.to_csv(file_path, index=False)
