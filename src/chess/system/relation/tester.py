from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import LoggingLevelRouter, RelationReport


P = TypeVar("P")
S = TypeVar("S")



class RelationTester(ABC, Generic[P, S]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def test(cls, candidate_primary: P, candidate_satellite: S) -> RelationReport[P, S]:
        pass