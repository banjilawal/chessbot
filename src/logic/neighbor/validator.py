# src/logic/neighbor/exception.py

"""
Module: logic.neighbor.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import Any, cast

from logic.neighbor import VisitationEvent, NullVisitationEventException
from logic.system import LoggingLevelRouter, ValidationResult, ValidationTransaction


class VisitationEventValidationTransaction(ValidationTransaction[VisitationEvent]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, candidate: Any) -> ValidationResult[VisitationEvent]:
        """"""
        method = "VisitationEventValidationTransaction.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVisitationEventException(f"{method}: {NullVisitationEventException.MSG}")
                )
            
            if not isinstance(candidate, VisitationEvent):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Visit, got {type(candidate)} instead")
                )
            event = cast(VisitationEvent, candidate)
            
            
            
            return ValidationResult.success(payload=event)
        except Exception as e:
            return ValidationResult.failure(e)
    


