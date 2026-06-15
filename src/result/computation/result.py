# src/result/computation/result.py

"""
Module: result.computation.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from result import ComputationState, Result

T = TypeVar("T")

class ComputationResult(Result[T], Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains outcome of a compute transaction.

    Attributes:
        exception: Optional[Exception]
        state: ComputationState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> ComputationResult
        -   def failure(exception: Exception) -> ComputationResult
        -   def timed_out(exception: Exception) -> ComputationResult
        
    Super Class:
        Result
    """
    _state: ComputationState
    
    def __init__(
            self,
            state: ComputationState,
            exception: Optional[Exception] = None,
            payload: Optional[T] = None,
    ):
        """
        Args:
            payload: Optional[T]
            state: ComputationState
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> ComputationState:
        return self._state

    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ComputationState.FAILURE or
                self._state == ComputationState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ComputationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ComputationResult:
        return cls(
            payload=payload,
            exception=None,
            state=ComputationState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ComputationResult:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ComputationResult:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationState.TIMED_OUT,
        )
