# src/artifact/result/play/result.py

"""
Module: artfifact.result.play.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import PlayState, Result
from domain import GameOutcome

T = TypeVar("T", bound="GameOutcome")


class PlayResult(Result[T], ABC, Generic[T]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains the outcome of a play transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        state: PlayResultState
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> PlayResult
        -   def failure(exception: Exception) -> PlayResult
        -   def timed_out(cls, exception: Exception) -> PlayResult:

    Super Class:
        Result
    """
    _state: PlayState
    
    
    def __init__(
            self,
            state: PlayState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: PlayResultState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use play methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[T]:
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
                self._state == PlayState.FAILURE or
                self._state == PlayState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == PlayState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> PlayResult:
        return cls(
            payload=payload,
            state=PlayState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> PlayResult:
        return cls(
            exception=exception,
            state=PlayState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> PlayResult:
        return cls(
            exception=exception,
            state=PlayState.TIMED_OUT,
        )