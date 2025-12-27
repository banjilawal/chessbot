from abc import ABC
from typing import Generic, TypeVar

from chess.system import Dyad, RelationResult

D = TypeVar("D", bound=Dyad)



class RelationEvaluator(ABC, Generic[D]):
    
    @classmethod
    def evaluate(cls, dyad: D) -> RelationResult:
        pass