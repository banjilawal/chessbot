from abc import ABC
from typing import Generic, TypeVar

from model import Report
from result import AnalysisResult
from system import LoggingLevelRouter

R = TypeVar("R", bound=Report)

class Analyst(ABC, Generic[R]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, *args, **kwargs) -> AnalysisResult[R]:
        pass