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
from exchange import Request

T = TypeVar("T", bound="Request")

class Decision(ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        permission: Permission
        request: Optional[T]
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(request: T) -> Decision[T]:
        -   def deny(exception: Exception) -> Exception

    Super Class:
    """
    _permission: Permission
    _request: Optional[T]
    _exception: Optional[Exception]
  
    def __init__(
            self,
            permission: Permission,
            request: Optional[T] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: Optional[T]
            exception: Optional[Exception]
        """
        self._request = request
        self._exception = exception
        self._permission = permission
    
    @property
    def request(self) -> Optional[T]:
        return self._request
        
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_granted(self) -> bool:
        return (
                self._exception is None and
                self._request is not None and
                self._permission == Permission.GRANTED
        )
    
    @property
    def is_denial(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant(cls, request: T) -> Decision[T]:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def denial(cls, exception: Exception) -> Decision[T]:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> Decision[T]:
        return cls(
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
