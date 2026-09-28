# src/artifact/result/attack/result.py

"""
Module: artfifact.result.attack.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import AttackState, Result
from domain import CheckmateEncounter, Encounter, EncounterWarning, KillEncounter

T = TypeVar("T", bound="Encounter")


class AttackResult(Result[Encounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a attack transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        state: attackState
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> AttackResult
        -   def failure(exception: Exception) -> AttackResult
        -   def timed_out(cls, exception: Exception) -> AttackResult:

    Super Class:
        Result
    """
    _state: AttackState
    
    def __init__(
            self,
            state: AttackState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: attackState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[T]:
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
    
    
    @property
    def is_kill(self) -> bool:
        return (
            self._payload is not None and
            self._exception is None and
            self._state == AttackState.COMBATANT_KILLED and
            isinstance(self._payload, KillEncounter)
        )
    
    @property
    def is_check_warning_issued(self) -> bool:
        return (
                self._payload is not None and
                self._exception is None and
                self._state == AttackState.COMBATANT_KILLED and
                isinstance(self._payload, EncounterWarning)
        )
    
    @property
    def is_checkmate(self) -> bool:
        return (
                self._payload is not None and
                self._exception is None and
                self._state == AttackState.CHECKMATE and
                isinstance(self._payload, CheckmateEncounter)
        )
    

    
    @classmethod
    def success(cls, payload: T) -> AttackResult:
        return cls(
            payload=payload,
            state=AttackState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> AttackResult:
        return cls(
            exception=exception,
            state=AttackState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> AttackResult:
        return cls(
            exception=exception,
            state=AttackState.TIMED_OUT,
        )