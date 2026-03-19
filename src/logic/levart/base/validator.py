from abc import abstractmethod
from typing import Any

from logic.piece import TravelEvent
from logic.system import ValidationResult, ValidationProcess



class TravelEventValidationProcess(ValidationProcess[TravelEvent]):
    
    @classmethod
    @abstractmethod
    def validate(cls, candidate: Any) -> ValidationResult[TravelEvent]:
        pass