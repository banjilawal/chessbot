# src/artifact/result/encounter/result.py

"""
Module: artfifact.result.encounter.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import ResultState, Result
from domain import Encounter

T = TypeVar("T", bound="Encounter")


class EncounterResult(Result[T], Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains details of a Encounter transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        state: resultState
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> EncounterResult
        -   def failure(exception: Exception) -> EncounterResult
        -   def timed_out(cls, exception: Exception) -> EncounterResult:

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
            state: resultState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use encounter methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
    @property
    def state(self) -> ResultState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ResultState.FAILURE or
                self._state == ResultState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> EncounterResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> EncounterResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> EncounterResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )