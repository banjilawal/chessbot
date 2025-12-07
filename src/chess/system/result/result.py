# src/chess/system/result/result.py

"""
Module: chess.system.result.result
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic
from chess.system import Result

T = TypeVar("T")


class Result(Generic[T]):
    """
    # ROLE: Message passing, Data Transfer Object
  
    # RESPONSIBILITIES:
    1. Carry the outcome of a entity_service access or entity_service generation operation to the caller.
    2. Transporting errors from the entity_service source to the requester for handling that preserves
        reliability and availability.
  
    # PROVIDES:
    1.
  
    # Attributes:
        *   payload (T)
        *   exception (Exception)
    """
    _payload: Optional[T]
    _exception: Optional[Exception]
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        self._payload = payload
        self._exception = exception
    
    @property
    def payload(self) -> Optional[T]:
        return self._payload
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None
    
    def is_failure(self) -> bool:
        return self._exception is not None
    
    def is_empty(self) -> bool:
        return self._payload is None and self._exception is None
    
    @classmethod
    def success(cls, payload: T) -> Result[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> Result[T]:
        return cls(exception=exception)
    
    @classmethod
    def empty(cls) -> Result[None]:
        return cls()
