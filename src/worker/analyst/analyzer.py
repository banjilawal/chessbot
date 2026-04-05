from abc import ABC
from typing import Generic, TypeVar

from result import Result
from system import LoggingLevelRouter

T = TypeVar("T")

class Analyzer(ABC, Generic[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, ) -> Result:
        pass