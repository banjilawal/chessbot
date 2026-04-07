# src/result/deletion/result.py

"""
Module: result.deletion.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from result import DeletionState, Result

T = TypeVar("T")


class DeletionResult(Result, Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a deletion.

    Attributes:
        exception: Optional[Exception]
        state: validationState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_nothing_to_delete: bool

    Provides:
        -   def success(payload: T) -> DeletionResu[T]
        -   def failure(exception: Exception) -> DeletionResu[T]
        -   def timed_out(exception: Exception) -> DeletionResult[T]
        -   def nothing_to_delete() -> DeletionResult[T]

    Super Class:
        Result
    """
    _state = DeletionState
    
    def __init__(
            self,
            state: DeletionState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[T]
            state: DeletionResultState
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> DeletionState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state == DeletionState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == DeletionState.FAILURE or
                self._state == DeletionState.TIMED_OUT
        )
    
    @property
    def is_nothing_to_delete(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state == DeletionState.NOTHING_TO_DELETE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == DeletionState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> DeletionResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=DeletionState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DeletionState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DeletionState.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_delete(cls) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=DeletionState.NOTHING_TO_DELETE,
        )

