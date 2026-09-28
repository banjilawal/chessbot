# src/artifact/result/attack/warning/result.py

"""
Module: artfifact.result.attack.warning.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, ResultState
from domain import EncounterWarning


class WarningResult(AttackResult[EncounterWarning]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a attack transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[EncounterWarning]
        state: resultState
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: EncounterWarning) -> WarningResult
        -   def failure(exception: Exception) -> WarningResult
        -   def timed_out(exception: Exception) -> WarningResult:

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[EncounterWarning] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[EncounterWarning]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[EncounterWarning]:
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
    def success(cls, payload: T) -> WarningResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> WarningResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> WarningResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )