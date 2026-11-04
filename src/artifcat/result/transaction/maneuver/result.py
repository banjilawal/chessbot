# src/artifact/result/transaction/maneuver/result.py

"""
Module: artfifact.result.transaction.maneuver.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, TypeVar, cast

from artifcat import ResultState, TransactionResult
from domain import Maneuver

T = TypeVar("T", bound="Maneuver")

class ManeuverResult(TransactionResult[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains the outcome of an Maneuver transaction.


    Attributes:
        state: resultState
        payload: Optional[T]
        exception: Optional[Exception]

    Provides:
        -   def success(payload: T) -> ManeuverResult

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
    def state(self) -> ResultState:
        return self._state
    
    @property
    def payload(self) -> Optional[T]:
        return cast(Maneuver, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self.state == ResultState.SUCCESS and
            isinstance(self.payload, Maneuver)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.success
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ManeuverResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ManeuverResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ManeuverResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )