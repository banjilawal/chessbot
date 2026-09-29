# src/artifact/result/maneuver/result.py
"""
Module: artfifact.result.maneuver.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Result, ResultState
from sync import Turn


class TurnResult(Result[Turn]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a Turn transaction.

    Attributes:
        exception: Optional[Exception]
        state: resultState
        payload: Optional[Turn]
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
    _state: ResultState
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[Turn] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[Turn]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use maneuver methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[Turn]:
        return cast(Turn, super().payload)
    
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
    def success(cls, payload: Turn) -> TurnResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> TurnResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> TurnResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )


