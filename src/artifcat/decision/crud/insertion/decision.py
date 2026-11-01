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
from exchange import InsertionPermissionRequest, InsertionRequest

P = TypeVar("P", bound="InsertionPermissionRequest")
T = TypeVar("T", bound="InsertionRequest")


class InsertionDecision(CrudDecision[P, T], ABC, Generic[P, T]):
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
            approval: Optional[T] | None = None,
            permission_request: Optional[P] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            approval: Optional[T]
            permission_request: Optional[P]
            exception: Optional[Exception]
        """
        super().__init__(
            approval=approval,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )
