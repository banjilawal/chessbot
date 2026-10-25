# src/artifact/result/authorizable/attack/result.py

"""
Module: artfifact.result.authorizable.attack.result.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import Authorizable, Result, ResultState
from domain import Encounter

T = TypeVar("T", bound="Encounter")

class AttackResult(Result[T], Authorizable, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains the outcome of an Attack transaction.


    Attributes:
        state: resultState
        payload: Optional[T]
        exception: Optional[Exception]
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

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
    
    @classmethod
    def success(cls, payload: T) -> AttackResult:
        return cls(payload=payload, state=ResultState.SUCCESS)