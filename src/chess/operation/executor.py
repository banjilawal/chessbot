from abc import abstractmethod, ABC

from chess.operation import Directive, ExecutionContext, OperationResult

class Executor(ABC):
    """Base class for operation execution handlers"""

    @staticmethod
    @abstractmethod
    def execute_directive(directive: Directive, context: ExecutionContext) -> OperationResult:
        pass
