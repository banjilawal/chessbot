from abc import ABC
from typing import Generic, TypeVar

from chess.system import Dyad, RelationReport

D = TypeVar("D", bound=Dyad)



class RelationTester(ABC, Generic[D]):
    
    @classmethod
    def test(cls, dyad: D) -> RelationReport:
        pass