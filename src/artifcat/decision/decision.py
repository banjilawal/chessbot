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
from exchange import PermissionRequest, TransactionRequest

T = TypeVar("T", bound="TransactionRequest")

class Decision(ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        permission_request: PermissionRequest[T]
        permission: Permission
        approval: Optional[T]
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(
                    approval: T,
                    permission_request: PermissionRequest[T],
            ) -> Decision[T]
            
        -   def denial(
                    permission_request: PermissionRequest[T],
                    exception: Exception,
            ) -> Decision[T]

    Super Class:
    """
    _permission_request: PermissionRequest[T]
    _permission: Permission
    _exception: Optional[Exception]
    _approval: Optional[TransactionRequest]
  
    def __init__(
            self,
            permission: Permission,
            permission_request: PermissionRequest[T],
            exception: Optional[Exception] | None = None,
            approval: Optional[TransactionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            approval: Optional[TransactionRequest]
        """
        self._approval = approval
        self._exception = exception
        self._permission = permission
        self._permission_request = permission_request
    
    @property
    def permission_request(self) -> PermissionRequest[T]:
        return self._permission_request
        
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def approval(self) -> Optional[T]:
        return 
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def request_is_granted(self) -> bool:
        return (
                self._exception is None and
                self._approval is not None and
                self._permission == Permission.GRANTED
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    
    @classmethod
    def grant(cls, approval: T, permission_request: PermissionRequest[T]) -> Decision[T]:
        return cls(
            approval=approval, 
            permission_request=permission_request, 
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(cls, permission_request: PermissionRequest[T], exception: Exception) -> Decision[T]:
        return cls(
            exception=exception,
            permission_request=permission_request,
            permission=Permission.DENIED,
        )
    
