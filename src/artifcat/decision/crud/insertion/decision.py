# src/artifact/decision/crud/insertion/decision.py

"""
Module: artfifact.decision.crud.insertion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import Permission
from artifcat.decision.crud import CrudDecision
from exchange import InsertionRequest, PermissionRequest

T = TypeVar("T", bound="InsertionRequest")

class InsertionDecision(CrudDecision[T], Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an insertion is permitted or denied.
        
    Attributes:
        permission: Permission
        permission_request: PermissionRequest[T]
        exception: Optional[Exception]
        approval: Optional[T]
        
    Provides:
        -   def grant(
                    approval: T,
                    permission_request: PermissionRequest[T],
            ) -> Decision[T]
            
        -   def denial(
                    permission_request: PermissionRequest[T],
                    exception: Exception,
            ) -> Decision[T]
            
        -   def do_nothing(
                    permission_request: PermissionRequest[T]
            ) -> InsertionDecision

    Super Class:
        CrudDecision
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
            approval: Optional[TransactionRequest]
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
        
    @property
    def item_already_exists(self):
        return (
            self.exception is None and
            self.approval is None and
            self.permission == Permission.DO_NOTHING
        )
    
    @classmethod
    def grant(
            cls,
            approval: T,
            permission_request: PermissionRequest[T],
    ) -> InsertionDecision[T]:
        return cls(
            approval=approval, 
            permission_request=permission_request, 
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(
            cls,
            permission_request: PermissionRequest[T],
            exception: Exception,
    ) -> InsertionDecision[T]:
        return cls(
            exception=exception,
            permission_request=permission_request,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def do_nothing(cls, permission_request: PermissionRequest[T],) -> InsertionDecision:
        return cls(
            permission_request=permission_request,
            permission=Permission.DO_NOTHING,
        )
    
