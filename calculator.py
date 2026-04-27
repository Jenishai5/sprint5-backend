import time
from models import OperationType


def calculate(num1: float, num2: float, operation: str):
    start = time.time()

    try:
        op = OperationType(operation)
    except ValueError:
        raise ValueError("Invalid operation")

    if op == OperationType.PLUS:
        result = num1 + num2
    elif op == OperationType.MINUS:
        result = num1 - num2
    elif op == OperationType.MULTIPLY:
        result = num1 * num2
    elif op == OperationType.DIVIDE:
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2

    duration = (time.time() - start) * 1000

    return result, duration
