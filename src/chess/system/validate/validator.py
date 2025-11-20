# src/chess/system/validate/team_stack_validator.py

"""
Module: chess.system.validate.team_stack_validator
Author: Banji Lawal
Created: 2025-09-28
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from chess.system import LoggingLevelRouter, ValidationResult

T = TypeVar("V")


class Validator(ABC, Generic[T]):
    """
    # ROLE: Validation, Data Integrity assurance.
  
    # RESPONSIBILITIES:
    1.  Verifies a candidate is an instance of V, that meets integrity requirements, before the candidate is used.
    2.  Returns any exceptions raised inside a ValidationResult
    
  
    # PROVIDES:
    ValidationResult[V] containing either:
        - On success: V in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[T]:
        """
        # ACTION:
        1.  Check if candidate is null.
        2.  Check if candidate is of type V.
        3.  Run integrity check on each of the candidate's attributes.
        4.  If any check fails, it raises an exception, return the exception inside a ValidationResult.
        3.  When all checks pass, cast candidate to V, then return it inside a ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any): Object to validate.
    
        # Returns:
        ValidationResult[V] containing either:
            - On success: V in the payload.
            - On failure: Exception.
    
        # RAISES:
            *   TypeError
            *   NullException
            *   ValidationException
        """
        pass
