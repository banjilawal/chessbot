
from typing import TypeVar

from operation import Operation
from result import InsertionResult
from stack import StackService
from util import LoggingLevelRouter

T = TypeVar("T")

class Pusher(Operation[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            item: T,
            stack: StackService[T],
            *args,
            **kwargs,
    ) -> InsertionResult:
        pass