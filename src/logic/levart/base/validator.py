from abc import abstractmethod
from typing import Any

from logic.piece import TravelEvent
from logic.system import ValidationResult, ValidationTransaction



class TravelEventValidationTransaction(ValidationTransaction[TravelEvent]):
    
    @classmethod
    @abstractmethod
    def execute(cls, candidate: Any) -> ValidationResult[TravelEvent]:
        pass