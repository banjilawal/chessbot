# src/result/insert/result.py

"""
Module: result.insert.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from result import InsertionState, Result


class InsertionResult(Result[bool]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of an insertion.

    Attributes:
        exception: Optional[Exception]
        state: validationState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> InsertionResu[T]
        -   def failure(exception: Exception) -> InsertionResu[T]
        -   def timed_out(exception: Exception) -> InsertionResult[T]

    Super Class:
        Result
    """
    _self: InsertionState
    
    def __init__(
            self,
            payload: bool,
            state: InsertionState,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: bool
            state: InsertionState
            exception: Optional[Exception]            
        """
        super().__init__(
            payload=payload, 
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> InsertionState:
        return self._state
        
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == InsertionState.FAILURE or
                self._state == InsertionState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == InsertionState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: bool = True) -> InsertionResult[bool]:
        return cls(
            payload=True,
            exception=None,
            state=InsertionState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> InsertionResult[bool]:
        return cls(
            payload=False,
            exception=exception,
            state=InsertionState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> InsertionResult[bool]:
        return cls(
            payload=False,
            exception=exception,
            state=InsertionState.TIMED_OUT,
        )

