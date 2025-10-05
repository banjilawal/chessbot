
from enum import Enum, auto
from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from chess.event import Event
from chess.system import ExecutionContext, TransactionResult

T = TypeVar('T', bound=Event)

class State(Enum):
  RUNNING = auto()
  TIMED_OUT = auto()
  ROLLED_BACK = auto()
  SUCCESS = auto()

class Transaction(ABC, Generic[T]):
  """Base class for transaction execution handlers"""

  @classmethod
  @abstractmethod
  def execute(cls, event: T, context: ExecutionContext) -> TransactionResult:
    pass
