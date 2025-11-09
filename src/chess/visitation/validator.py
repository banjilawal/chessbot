# src/chess/visitation/factory.py

"""
Module: chess.visitation.validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import Any, cast

from chess.visitation import VisitationEvent, NullVisitationEventException
from chess.system import LoggingLevelRouter, ValidationResult, Validator


class VisitationEventValidator(Validator[VisitationEvent]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[VisitationEvent]:
        """"""
        method = "VisitationEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVisitationEventException(f"{method}: {NullVisitationEventException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, VisitationEvent):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Visit, got {type(candidate)} instead")
                )
            event = cast(VisitationEvent, candidate)
            
            
            
            return ValidationResult.success(payload=event)
        except Exception as e:
            return ValidationResult.failure(e)
    


