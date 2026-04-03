# src/result/validation/result.py
"""
Module: result.validation.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, TypeVar, Generic
from logic.system import MethodImplementationException, Result

T = TypeVar("T")

class ValidationResult(Result[T], Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a validation transaction.

    Attributes:
        exception: Optional[Exception]
        state: buildState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result[T]
        -   def failure(exception: Exception) -> Result[T]

    Super Class:
        Result
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
            exception=MethodImplementationException(
                f"{method}: {MethodImplementationException.MSG}. ValidationResult cannot"
                f" be empty. It must have either a payload or an rollback_exception."
            )
        )


