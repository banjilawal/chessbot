from abc import ABC
from typing import Generic, TypeVar


from result import InsertionResult
from stack import StackService
from util import LoggingLevelRouter

T = TypeVar("T")

class Pusher(ABC, Generic[T]):
    
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