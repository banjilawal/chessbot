# src/result/result.py

"""
Module: result.result
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
        1.  Hold the product of some work.

    Attributes:
        payload: Optional[T]
        exception: Optional[Exception]
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result
        -   def failure(exception: Exception) -> Result
        
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
    def success(cls, payload: T) -> Result:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> Result:
        return cls(exception=exception)
    
