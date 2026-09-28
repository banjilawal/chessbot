# src/artifact/result/play/kill/result.py

"""
Module: artfifact.result.play.kill.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayResult, PlayState
from domain import KillEncounter


class KillResult(PlayResult[KillEncounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a play transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[KillEncounter]
        state: playState
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: KillEncounter) -> KillResult
        -   def failure(exception: Exception) -> KillResult
        -   def timed_out(exception: Exception) -> KillResult:

    Super Class:
        PlayResult
    """
    
    def __init__(
            self,
            state: PlayState,
            payload: Optional[KillEncounter] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: playState
            payload: Optional[KillEncounter]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use play methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[KillEncounter]:
        return cast(T, super().payload)
    
    @property
    def state(self) -> PlayState:
        return self._state
        
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  PlayState.FAILURE or
                self._state ==  PlayState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  PlayState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> KillResult:
        return cls(
            payload=payload,
            state=PlayState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> KillResult:
        return cls(
            exception=exception,
            state=PlayState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> KillResult:
        return cls(
            exception=exception,
            state=PlayState.TIMED_OUT,
        )