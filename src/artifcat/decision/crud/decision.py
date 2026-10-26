# src/artifact/decision/crud/decision.py

"""
Module: artfifact.decision.crud.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import Decision, Permission
from exchange import PermissionRequest

T = TypeVar("T", bound="CrudTransactionRequest")

class CrudDecision(Decision[T], ABC, Generic[T]):
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
        Decision
    """
  
    def __init__(
            self,
            permission: Permission,
            permission_request: PermissionRequest[T],
            exception: Optional[Exception] | None = None,
            approval: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            approval: Optional[T]
        """
        super().__init__(
            approval=approval,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )
    
    @property
    def permission_request(self) -> PermissionRequest[T]:
        return cast(PermissionRequest[T], super().permission_request)
    
    @property
    def approval(self) -> Optional[T]:
        return cast(T, super().approval)
    
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
    
