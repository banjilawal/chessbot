# src/artifact/result/attack/stalemate/result.py

"""
Module: artfifact.result.attack.stalemate.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, AttackState
from domain import StalemateEncounter


class StalemateResult(AttackResult[StalemateEncounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a attack transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[StalemateEncounter]
        state: attackState
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: StalemateEncounter) -> StalemateResult
        -   def failure(exception: Exception) -> StalemateResult
        -   def timed_out(exception: Exception) -> StalemateResult:

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: AttackState,
            payload: Optional[StalemateEncounter] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: attackState
            payload: Optional[StalemateEncounter]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[StalemateEncounter]:
        return cast(T, super().payload)
    
    @property
    def state(self) -> AttackState:
        return self._state
        
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  AttackState.FAILURE or
                self._state ==  AttackState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  AttackState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> StalemateResult:
        return cls(
            payload=payload,
            state=AttackState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> StalemateResult:
        return cls(
            exception=exception,
            state=AttackState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> StalemateResult:
        return cls(
            exception=exception,
            state=AttackState.TIMED_OUT,
        )