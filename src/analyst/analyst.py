from abc import ABC
from typing import Generic, TypeVar

from result import ComputationResult, Result
from system import LoggingLevelRouter

T = TypeVar("T")

class Analyst(ABC, Generic[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, ) -> ComputationResult[Report]:
        pass