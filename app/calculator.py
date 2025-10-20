from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.observers import LoggingObserver, AutoSaveObserver
import copy

class Calculator:
    def __init__(self):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.observers = [LoggingObserver(), AutoSaveObserver(self)]  # 👈 Add observers

    def calculate(self, operation_name: str, a: float, b: float) -> float:
        self._save_state_for_undo()
        operation = OperationFactory.get_operation(operation_name, a, b)
        result = operation.execute()
        calc = Calculation(operation_name, a, b, result)
        self.history.append(calc)
        self.redo_stack.clear()

        # 👇 Notify all observers
        for observer in self.observers:
            observer.update(calc)

        return result

    def _save_state_for_undo(self):
        snapshot = copy.deepcopy(self.history)
        self.undo_stack.append(CalculatorMemento(snapshot))

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(CalculatorMemento(copy.deepcopy(self.history)))
        memento = self.undo_stack.pop()
        self.history = memento.get_saved_state()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(CalculatorMemento(copy.deepcopy(self.history)))
        memento = self.redo_stack.pop()
        self.history = memento.get_saved_state()

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
