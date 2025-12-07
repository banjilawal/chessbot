# src/chess/system/validate/result/result.py

"""
Module: chess.system.validate.result.result
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic
from chess.system import NotImplementedException, Result

T = TypeVar("T")


class ValidationResult(Result[Generic[T]]):
    """
    # ROLE: Message passing, Data Transfer Object
  
    # RESPONSIBILITIES:
    1. Carry the outcome a coord_stack_validator operation to originating client.
    2. Enforcing mutual exclusion. A ValidationResult can either carry _payload or _exception. Not both.
  
    # PROVIDES:
    1. A correctness verification or denial for the Validation entity_service provider.
  
    # ATTRIBUTES:
      * See Result superclass for attributes.
    """
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "ValidationResult.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. ValidationResult cannot"
                f" be empty. It must have either a payload or an rollback_exception."
            )
        )
