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
from exchange import PermissionRequest, CrudPermissionRequest, CrudRequest

T = TypeVar("T", bound="CrudRequest")


class CrudDecision(Decision[T], ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[T]

    Provides:
        -   def grant(
                    approval: CrudRequest,
                    permission_request: PermissionRequest,
            ) -> CrudDecision[T]

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> CrudDecision[T]

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            permission_request: CrudPermissionRequest[T],
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
            approval: CrudRequest,
            permission_request: PermissionRequest,
    ) -> CrudDecision:
        role_request = cast(
            CrudPermissionRequest,
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


    
