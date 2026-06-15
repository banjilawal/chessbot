# src/result/build/result.py

"""
Module: result.build.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypeVar, Generic

T = TypeVar("T")

@dataclass
class Result(Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport
  
    Responsibilities:
        1.  Contains the outcome of a transaction. Either a work product or
            an exception.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result[T]
        -   def failure(exception: Exception) -> Result[T]
        
    Super Class:
    """
    _payload: Optional[T]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None
    ):
        """
        Args:
            payload: Optional[T]
            exception: Optional[Exception]
        """
        self._payload = payload
        self._exception = exception
    
    @property
    def payload(self) -> Optional[T]:
        return self._payload
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None
    
    @property
    def is_failure(self) -> bool:
        return self._exception is not None
    
    @classmethod
    def success(cls, payload: T) -> Result[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> Result[T]:
        return cls(exception=exception)
    
