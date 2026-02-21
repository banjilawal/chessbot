# src/chess/system/validate/result/result.py

"""
Module: chess.system.validate.result.result
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic
from chess.system import MethodNotImplementedException, Result, ValidationResult

T = TypeVar("T")


class ValidationResult(Result[T], Generic[T]):
    """
    # ROLE: Messanger Data Transport Object, Error Transport Object.
  
    # RESPONSIBILITIES:
    1. Send the outcome of a validation request to the client.
    2. Enforcing mutual exclusion. A ValidationResult can either carry payload or exception. Not both.
    
    # PARENT:
        *   Result
  
    # PROVIDES:
    NOne
  
    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
    """
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def success(cls, payload: T) -> ValidationResult[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> ValidationResult[T]:
        return cls(exception=exception)
    
    @classmethod
    def empty(cls) -> ValidationResult[T]:
        method = "ValidationResult.empty"
        return cls(
            exception=MethodNotImplementedException(
                f"{method}: {MethodNotImplementedException.DEFAULT_MESSAGE}. ValidationResult cannot"
                f" be empty. It must have either a payload or an rollback_exception."
            )
        )


