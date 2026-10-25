# src/artifact/decision/decision.py

"""
Module: artfifact.decision.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import Permission
from exchange import PermissionRequest

T = TypeVar("T", bound="PermissionRequest")

class Decision(ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        transaction_request: T
        permission: Permission
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(cls, request: T) -> Decision[T]:
        -   def deny(exception: Exception) -> Exception

    Super Class:
    """
    _transaction_request: T
    _permission: Permission
    _exception: Optional[Exception]
  
    def __init__(
            self,
            transaction_request: T,
            permission: Permission,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            transaction_request: T
            permission: Permission
            exception: Optional[Exception]
        """
        self._transaction_request = transaction_request
        self._exception = exception
        self._permission = permission
    
    @property
    def transaction_request(self) -> T:
        return self._transaction_request
        
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def request_is_granted(self) -> bool:
        return (
                self._exception is None and
                self._transaction_request is not None and
                self._permission == Permission.GRANTED
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    
    @classmethod
    def grant(cls, request: T) -> Decision[T]:
        return cls(transaction_request=request, permission=Permission.GRANTED)
    
    @classmethod
    def denial(cls, request: T, exception: Exception) -> Decision[T]:
        return cls(
            transaction_request=request,
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, request: T, exception: Exception) -> Decision[T]:
        return cls(
            transaction_request=request,
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
