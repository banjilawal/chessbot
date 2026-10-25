# src/artifact/result.transaction.computation/result.py

"""
Module: artfifact.result.transaction.computation.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import ResultState, TransactionResult

T = TypeVar("T")

class ComputationResult(TransactionResult[T], TransactionResult, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains the outcome of an Computation transaction.


    Attributes:
        state: resultState
        payload: Optional[T]
        exception: Optional[Exception]

    Provides:
        -   def success(payload: T) -> ComputationResult

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
        super().__init__(state=state, payload=payload, exception=exception)
    
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
