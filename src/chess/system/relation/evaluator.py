from abc import ABC
from typing import Generic, TypeVar

from chess.system import Dyad, RelationReport

D = TypeVar("D", bound=Dyad)



class RelationEvaluator(ABC, Generic[D]):
    
    @classmethod
    def evaluate(cls, dyad: D) -> RelationReport:
        pass