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

T = TypeVar("T")

class Decision(ABC, Generic[T]):
    """
    Role:
        - Authorization Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        permission: Permission
        exception: Optional[Exception]
        is_denied: bool
        is_granted
        
    Provides:
        - def deny(exception: Exception) -> Exception

    Super Class:
    """
    _permission: Permission
    _exception: Optional[Exception]
  
    def __init__(self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
        """
        self._exception = exception
        self._permission = permission
        
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
        return not self.is_granted
    
    @classmethod
    def deny(cls, exception: Exception) -> Decision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
