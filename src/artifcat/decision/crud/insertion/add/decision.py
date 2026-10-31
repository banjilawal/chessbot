# src/artifact/decision/crud/insertion/add/decision.py

"""
Module: artfifact.decision.crud.insertion.add.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from artifcat import InsertionDecision, Permission
from exchange import (
    AddNodeRequest, InsertionRequest, PermissionRequest, CrudPermissionRequest,
)

T = TypeVar("T", bound="AddNodeRequest")

class AddNodeDecision(InsertionDecision[T], Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[AddRequest]

    Provides:
        -   def grant(
                    approval: AddRequest,
                    permission_request: PermissionRequest,
            ) -> AddDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> AddDecision

    Super Class:
        InsertionDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            permission_request: AddNodePermissionRequest[T],
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
            permission_request=permission_request,
            approval=approval,
            exception=exception,
            permission=permission,
        )
        
    @property
    def approval(self) -> T:
        return cast(T, super().approval)
    
    @classmethod
    def grant(
            cls, 
            approval: InsertionRequest,
            permission_request: PermissionRequest,
    ) -> InsertionDecision:
        role_request = cast(
            AddNodePermissionRequest,
            permission_request,
        )
        return cls(
            approval=approval,
            permission_request=role_request,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(
            cls, 
            permission_request: PermissionRequest,
            exception: Exception,
    ) -> InsertionDecision:
        role_request = cast(
            CrudPermissionRequest,
            permission_request,
        )
        return cls(
            exception=exception,
            permission_request=role_request,
            permission=Permission.DENIED,
        )


    
