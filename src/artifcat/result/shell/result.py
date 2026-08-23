# src/artifact/result/result.py

"""
Module: artfifact.result.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, TypeVar, Generic, cast

from artifcat.result import Result

T = TypeVar("T", bound="Command")


class ShellResult(Result, ABC, Generic[T]):
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
        Result
    """
    
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
        super().__init__(payload=payload, exception=exception)
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
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
    
