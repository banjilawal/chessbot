# src/artifact/result/result.py

"""
Module: artfifact.result.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, TypeVar, Generic

from artifcat import ResultState

T = TypeVar("T")


class Result(Generic[T]):
    """
    Role:
        - Data Transport
        - Error Transport
  
    Responsibilities:
        1.  Hold the product of some work.

    Attributes:
        state: ResultState
        payload: Optional[T]
        exception: Optional[Exception]
        
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result
        -   def failure(exception: Exception) -> Result
        
    Super Class:
    """
    
    _state: ResultState
    _payload: Optional[T]
    _exception: Optional[Exception]
    
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
        self._state = state
        self._payload = payload
        self._exception = exception
        
    @property
    def state(self) -> ResultState:
        return  self._state
    
    @property
    def payload(self) -> Optional[T]:
        return self._payload
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return (
                self._exception is None and
                self._payload is not None and
                self.state == ResultState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return self._exception is not None
    
    @classmethod
    def success(cls, payload: T) -> Result:
        return cls(payload=payload, state=ResultState.SUCCESS)
    
    @classmethod
    def failure(cls, exception: Exception) -> Result:
        return cls(exception=exception, state=ResultState.FAILURE)
    
