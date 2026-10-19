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
        - Authorization Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        request: T
        permission: Permission
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def deny(exception: Exception) -> Exception

    Super Class:
    """
    _request: T
    _permission: Permission
    _exception: Optional[Exception]
  
    def __init__(
            self,
            request: T,
            permission: Permission,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            request: T
            permission: Permission
            exception: Optional[Exception]
        """
        self._request = request
        self._exception = exception
        self._permission = permission
    
    @property
    def request(self) -> T:
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
                self._permission == Permission.GRANTED
        )
    
    @property
    def is_denied(self) -> bool:
        return (
            self._exception is not None and
            (
                    self._permission == Permission.DENIED or
                    self._permission == Permission.TIMED_OUT
            )
        )
    
    @classmethod
    def grant(cls, request: T) -> Decision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, request: T, exception: Exception) -> Decision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, request: T, exception: Exception) -> Decision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
