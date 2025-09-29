from abc import abstractmethod, ABC
from enum import Enum, auto
from typing import Generic, TypeVar

from chess.transaction import Event, ExecutionContext, TransactionResult

T = TypeVar('T', bound=Event)

class State(Enum):
    RUNNING = auto()
    TIMED_OUT = auto()
    ROLLED_BACK = auto()
    SUCCESS = auto()

class Transaction(ABC, Generic[T]):
    """Base class for transaction execution handlers"""

    @staticmethod
    @abstractmethod
    def execute(event: T, context: ExecutionContext) -> TransactionResult:
        pass
