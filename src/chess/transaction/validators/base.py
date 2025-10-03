from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system.result.transaction import TransactionResult

T = TypeVar('T')

class RequestValidator(ABC):


    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> TransactionResult:
        pass