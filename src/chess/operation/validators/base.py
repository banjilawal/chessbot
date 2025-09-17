from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.operation.op_result import OperationResult

T = TypeVar('T')

class RequestValidator(ABC):


    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> OperationResult:
        pass