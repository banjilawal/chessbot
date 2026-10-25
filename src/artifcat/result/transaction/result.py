# src/artifact/result/transaction/result.py

"""
Module: artfifact.result.transaction.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, TypeVar, cast

from artifcat import Result, ResultState, Transactional

T = TypeVar("T")


class TransactionResult(Result[T], Transactional):
    """
    Role:
        -   Persistence
  
    Responsibilities:
        1.  Hold the product of some work.

    Attributes:
        payload: Optional[T]

    Provides:
        -   def success(payload: T) -> TransactionResult
        
    Super Class:
        Result
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[T] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResultState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(state=state, payload=payload, exception=exception)
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @classmethod
    def success(cls, payload: T) -> TransactionResult:
        return cls(payload=payload, state=ResultState.SUCCESS)
    
