# src/artifact/result/computation/result.py

"""
Module: artfifact.result.computation.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import ResultState, Result, Resultable

T = TypeVar("T")

class ComputationResult(Result[T], Resultable, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains details of a Computation transaction.

    Attributes:
        state: resultState
        payload: Optional[T]
        exception: Optional[Exception]
        
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
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: ResultState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)

    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
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
    def success(cls, payload: T) -> ComputationResult:
        return cls(
            payload=payload,
            exception=None,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ComputationResult:
        return cls(
            payload=None,
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ComputationResult:
        return cls(
            payload=None,
            exception=exception,
            state=ResultState.TIMED_OUT,
        )
