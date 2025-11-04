# src/chess/graph/visitation/validator.py

"""
Module: chess.graph.visitation.validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import Any, cast

from chess.graph import NullVisitException, Visitation, VisitNullException
from chess.system import LoggingLevelRouter, ValidationResult, Validator


class VisitationValidator(Validator[Visitation]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Visitation]:
        """"""
        method = "VisitationValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVisitException(f"{method}: {NullVisitException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Visitation):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Visit, got {type(candidate)} instead")
                )
            visit = cast(Visitation, candidate)
            
            
            
            return ValidationResult.success(payload=visit)
        except Exception as e:
            return ValidationResult.failure(e)
    


