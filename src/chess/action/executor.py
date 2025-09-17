from abc import abstractmethod, ABC

from chess.action import Directive, ExecutionContext, OperationResult

class Executor(ABC):
    """Base class for action execution handlers"""

    @staticmethod
    @abstractmethod
    def execute_directive(directive: Directive, context: ExecutionContext) -> OperationResult:
        pass
