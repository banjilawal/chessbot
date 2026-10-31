# src/artifact/decision/crud/insertion/decision.py

"""
Module: artfifact.decision.crud.insertion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudDecision, Permission
from exchange import (
    PermissionRequest, CrudPermissionRequest, InsertionPermissionRequest, InsertionRequest
)


T = TypeVar("T", bound="InsertionRequest")

class InsertionDecision(CrudDecision[T], ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[InsertionRequest]

    Provides:
        -   def grant(
                    approval: InsertionRequest,
                    permission_request: PermissionRequest,
            ) -> InsertionDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
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
            approval: Optional[T]
        """
        super().__init__(
            permission_request=permission_request,
            approval=approval,
            exception=exception,
            permission=permission,
        )
    
    @classmethod
    def grant(
            cls, 
            approval: InsertionRequest,
            permission_request: PermissionRequest,
    ) -> CrudDecision:
        role_request = cast(
            InsertionPermissionRequest,
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
    ) -> CrudDecision:
        role_request = cast(
            CrudPermissionRequest,
            permission_request,
        )
        return cls(
            exception=exception,
            permission_request=role_request,
            permission=Permission.DENIED,
        )


    
