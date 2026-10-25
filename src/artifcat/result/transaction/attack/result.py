# src/artifact/result/transaction/attack/result.py
"""
Module: artfifact.result.transaction.attack.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import Result, ResultState, Transactional
from domain import Encounter

T = TypeVar("T", bound="Encounter")


class AttackResult(Result[T], Transactional, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains the outcome of an Attack transaction.


    Attributes:
        state: resultState
        payload: Optional[T]
        exception: Optional[Exception]

    Provides:
        -   def success(payload: T) -> AttackResult

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
        super().__init__(state=state, payload=payload, exception=exception)
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
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
    def success(cls, payload: T) -> AttackResult[T]:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> AttackResult[T]:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> AttackResult[T]:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )


