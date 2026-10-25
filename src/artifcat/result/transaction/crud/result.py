# src/artifact/result/transaction/crud/result.py

"""
Module: artfifact.result.transaction.crud.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, TypeVar, Generic

from artifcat import Transactional

T = TypeVar("T")


class CrudResult(ABC, Transactional, Generic[T]):
    """
    Role:
        -   Persistence
  
    Responsibilities:
        1.  Contains details of a CRUD transaction.

    Attributes:
        payload: Optional[T]
        exception: Optional[Exception]
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result
        -   def failure(exception: Exception) -> Result
        
    Super Class:
        TransactionResult
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
    def exception(self) -> Optional:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None
    
    @property
    def is_failure(self) -> bool:
        return self._exception is None
    
    @classmethod
    def success(cls, payload: T) -> CrudResult[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> CrudResult:
        return cls(exception=exception)
    
