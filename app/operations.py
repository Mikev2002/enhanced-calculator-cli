class Operation:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError("Subclasses must implement execute()")


class Add(Operation):
    def execute(self):
        return self.a + self.b


class Subtract(Operation):
    def execute(self):
        return self.a - self.b


class Multiply(Operation):
    def execute(self):
        return self.a * self.b


class Divide(Operation):
    def execute(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b


class Power(Operation):
    def execute(self):
        return self.a ** self.b


class Root(Operation):
    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot take 0th root")
        return self.a ** (1 / self.b)


class Modulus(Operation):
    def execute(self):
        return self.a % self.b


class IntDivide(Operation):
    def execute(self):
        return self.a // self.b


class Percent(Operation):
    def execute(self):
        return (self.a / self.b) * 100


class AbsDiff(Operation):
    def execute(self):
        return abs(self.a - self.b)


# Factory
class OperationFactory:
    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntDivide,
        "percent": Percent,
        "abs_diff": AbsDiff,
    }

    @staticmethod
    def get_operation(name: str, a: float, b: float) -> Operation:
        op_class = OperationFactory.operations.get(name)
        if not op_class:
            raise ValueError(f"Unknown operation: {name}")
        return op_class(a, b)
