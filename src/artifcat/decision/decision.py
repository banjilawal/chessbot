# src/artifact/decision/decision.py

"""
Module: artfifact.decision.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Self, TypeVar

from artifcat import Permission
from exchange import PermissionRequest, TransactionRequest

P = TypeVar("P", bound="PermissionRequest")
T = TypeVar("T", bound="TransactionRequest")

class Decision(ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        permission_request: Optional[P] | None = None
        permission: Permission
        approval: Optional[T]
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(
                    approval: T,
                    permission_request: Optional[P] | None = None,
            ) -> Decision[T]
            
        -   def denial(
                    permission_request: Optional[P] | None = None,
                    exception: Exception,
            ) -> Decision[T]

    Super Class:
    """

    _permission: Permission
    _exception: Optional[Exception]
    _transaction_request: Optional[T]
    _permission_request: Optional[P]
  
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[P] | None = None,
            transaction_request: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[PermissionRequest]
            transaction_request: Optional[TransactionRequest]
        """
        self._exception = exception
        self._permission = permission
        self._permission_request = permission_request
        self._transaction_request = transaction_request
    
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def permission_request(self) -> Optional[P]:
        return self._permission_request
    
    @property
    def transaction_request(self) -> Optional[T]:
        return self._transaction_request
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def request_is_granted(self) -> bool:
        return (
                self._exception is None and
                self._transaction_request is not None and
                self._permission_request is not None and
                self._permission == Permission.GRANTED
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    
    @classmethod
    def grant(cls, approval: T, permission_request: P) -> Self:
        return cls(
            transaction_request=approval,
            permission_request=permission_request, 
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(cls, exception: Exception) -> Self:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )
    
