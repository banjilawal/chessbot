# src/logic/system/validate/validation.py

"""
Module: logic.system.validate.validation
Author: Banji Lawal
Created: 2025-09-28
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from logic.system import LoggingLevelRouter, ValidationResult

T = TypeVar("T")


class ValidationProcess(ABC, Generic[T]):
    """
     Role:Worker:
     # Task: Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure an object is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
    None

    # PROVIDES:
        * ValidationProcess


    # INHERITED ATTRIBUTES:
    None
    """
    def __init__(self):
        pass
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, candidate: Any, *args, **kwargs) -> ValidationResult[T]:
        """
        # ACTION:
        1.  CheckSquare if candidate is validation.
        2.  CheckSquare if candidate is of type V.
        3.  Run integrity check on each of the candidate's attributes.
        4.  If any check fails, it raises an exception, return the exception inside a ValidationResult.
        3.  When all checks pass, cast candidate to V, then return it inside a ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any): Object to validate.
    
        # RETURNS:
        ValidationResult[V] containing either:
            - On success: V in the payload.
            - On failure: Exception.
    
        Raises:
            *   TypeError
            *   NullException
            *   ValidationException
        """
        pass
