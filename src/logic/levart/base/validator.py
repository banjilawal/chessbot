from abc import abstractmethod
from typing import Any

from logic.piece import TravelEvent
from logic.system import ValidationResult, Validator



class TravelEventValidator(Validator[TravelEvent]):
    
    @classmethod
    @abstractmethod
    def validate(cls, candidate: Any) -> ValidationResult[TravelEvent]:
        pass