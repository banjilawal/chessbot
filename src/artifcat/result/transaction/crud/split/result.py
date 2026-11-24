# src/artifact/result/transaction/crud/split/result.py

"""
Module: artfifact.result.transaction.crud.split.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudResult, SplitState

T = TypeVar("T")


class SplitResult(CrudResult[T], Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains details of a Split transaction.

    Attributes:
        exception: Optional[Exception]
        state: resultState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_nothing_to_delete: bool

    Provides:
        -   def success(payload: T) -> SplitResu[T]
        -   def failure(exception: Exception) -> SplitResu[T]
        -   def timed_out(exception: Exception) -> SplitResult
        -   def nothing_to_delete() -> SplitResult

    Super Class:
        Result
    """
    _state = SplitState
    
    def __init__(
            self,
            state: SplitState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[T]
            state: SplitResultState
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
    def state(self) -> SplitState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state ==  SplitState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  SplitState.FAILURE or
                self._state ==  SplitState.TIMED_OUT
        )
    
    @property
    def is_nothing_to_delete(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state ==  SplitState.NOTHING_TO_DELETE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state ==  SplitState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> SplitResult:
        return cls(
            payload=payload,
            exception=None,
            state=SplitState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> SplitResult:
        return cls(
            payload=None,
            exception=exception,
            state=SplitState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> SplitResult:
        return cls(
            payload=None,
            exception=exception,
            state=SplitState.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_delete(cls) -> SplitResult:
        return cls(
            payload=None,
            exception=None,
            state=SplitState.NOTHING_TO_DELETE,
        )

