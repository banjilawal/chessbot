# src/artifact/result/validation/result.py
"""
Module: artfifact.result.validation.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import Result

T = TypeVar("T")


class ValidationResult(Result[T], Generic[T]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a validation transaction.

    Attributes:
        exception: Optional[Exception]
        state: resultState
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
    _state: ResultState
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
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
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
    @property
    def state(self) -> ResultState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.exception is None and
            self.payload is not None and
            self._state ==  ResultState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  ResultState.FAILURE or
                self._state ==  ResultState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ValidationResult[T]:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ValidationResult[T]:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ValidationResult[T]:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )


