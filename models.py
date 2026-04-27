from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class OperationType(Enum):
    PLUS = "plus"
    MINUS = "minus"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


@dataclass
class HistoryEntry:
    num1: float
    num2: float
    operation: str
    result: float
    timestamp: str
    duration_ms: float
