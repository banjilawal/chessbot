from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from chess.operation import Directive, ExecutionContext, OperationResult

T = TypeVar('T', bound=Directive)

class OperationExecutor(ABC, Generic[T]):
    """Base class for operation execution handlers"""

    @staticmethod
    @abstractmethod
    def execute_directive(directive: T, context: ExecutionContext) -> OperationResult:
        pass
