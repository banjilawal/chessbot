from abc import abstractmethod
from typing import Any

from chess.piece import TravelEvent
from chess.system import ValidationResult, Validator



class TravelEventValidator(Validator[TravelEvent]):
    
    @classmethod
    @abstractmethod
    def validate(cls, candidate: Any) -> ValidationResult[TravelEvent]:
        pass