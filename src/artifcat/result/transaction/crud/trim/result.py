# src/artifact/result/transaction/crud/trim/result.py

"""
Module: artfifact.result.transaction.crud.trim.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudResult, TrimState
from collection import DataStruct
from domain import Context

T = TypeVar("T", bound="DataStruct")


class TrimResult(CrudResult[T], Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains details of a Trim transaction.

    Attributes:
        exception: Optional[Exception]
        state: resultState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_nothing_to_delete: bool

    Provides:
        -   def success(payload: T) -> TrimResu[T]
        -   def failure(exception: Exception) -> TrimResu[T]
        -   def timed_out(exception: Exception) -> TrimResult
        -   def nothing_to_delete() -> TrimResult

    Super Class:
        Result
    """
    _state = TrimState
    
    def __init__(
            self,
            state: TrimState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[T]
            state: TrimResultState
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        super().__init__(payload=payload, exception=exception)
        self._state = state
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
        
    @property
    def state(self) -> TrimState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state ==  TrimState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  TrimState.FAILURE or
                self._state ==  TrimState.TIMED_OUT
        )
    
    @property
    def is_nothing_to_trim(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state ==  TrimState.NOTHING_TO_TRIM
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  TrimState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> TrimResult:
        return cls(
            payload=payload,
            exception=None,
            state=TrimState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> TrimResult:
        return cls(
            payload=None,
            exception=exception,
            state=TrimState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> TrimResult:
        return cls(
            payload=None,
            exception=exception,
            state=TrimState.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_trim(cls) -> TrimResult:
        return cls(
            payload=None,
            exception=None,
            state=TrimState.NOTHING_TO_TRIM,
        )

