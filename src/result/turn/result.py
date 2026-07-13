# src/result/maneuver/result.py
"""
Module: result.maneuver.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from model import Attack, Maneuver
from result import Result
from result.turn import ManeuverState

T = TypeVar("T", Maneuver, Attack)


class TurnResult(Result[T], Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a maneuver transaction.

    Attributes:
        exception: Optional[Exception]
        state: maneuverState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> DeletionResult[T]
        -   def failure(exception: Exception) -> DeletionResult[T]
        -   def timed_out(exception: Exception) -> ManeuverResult[T]:

    Super Class:
        Result
    """
    _state: ManeuverState
    
    def __init__(
            self,
            state: ManeuverState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: maneuverState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use maneuver methods instead of direct constructor."""
        self._state = state
    
    @property
    def state(self) -> ManeuverState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.exception is None and
            self.payload is not None and
            self._state == ManeuverState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ManeuverState.FAILURE or
                self._state == ManeuverState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ManeuverState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> TurnResult:
        return cls(
            payload=payload,
            state=ManeuverState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> TurnResult:
        return cls(
            exception=exception,
            state=ManeuverState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> TurnResult:
        return cls(
            exception=exception,
            state=ManeuverState.TIMED_OUT,
        )


