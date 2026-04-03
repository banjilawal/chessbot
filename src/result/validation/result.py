# src/result/validation/result.py
"""
Module: result.validation.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from result import Result
from result.validation import ValidationState

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
        state: validationState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> DeletionResult[T]
        -   def failure(exception: Exception) -> DeletionResult[T]
        -   def timed_out(exception: Exception) -> ValidationResult[T]:

    Super Class:
        Result
    """
    _state: ValidationState
    
    def __init__(
            self,
            state: ValidationState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: validationState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use validation methods instead of direct constructor."""
        self._state = state
    
    @property
    def state(self) -> ValidationState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ValidationState.FAILURE or
                self._state == ValidationState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ValidationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ValidationResult[T]:
        return cls(
            payload=payload,
            state=ValidationState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ValidationResult[T]:
        return cls(
            exception=exception,
            state=ValidationState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ValidationResult[T]:
        return cls(
            exception=exception,
            state=ValidationState.TIMED_OUT,
        )


