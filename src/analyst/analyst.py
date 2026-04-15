from abc import ABC
from typing import Generic, TypeVar

from analyst import Report
from result import AnalystResult
from system import LoggingLevelRouter

R = TypeVar("R", bound=Report)

class Analyst(ABC, Generic[R]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, *args, **kwargs) -> AnalystResult[R]:
        pass