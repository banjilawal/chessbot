# src/artifact/decision/crud/deletion/decision.py

"""
Module: artfifact.decision.crud.deletion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudDecision, Permission
from exchange import DeletionPermissionRequest, DeletionRequest

P = TypeVar("P", bound="DeletionPermissionRequest")
T = TypeVar("T", bound="DeletionRequest")


class DeletionDecision(CrudDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[DeletionRequest]

    Provides:
        -   def grant(
                    transaction_request: DeletionRequest,
                    permission_request: PermissionRequest,
            ) -> DeletionDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> DeletionDecision

    Super Class:
        CrudDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[T] | None = None,
            permission_request: Optional[P] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            transaction_request: Optional[T]
            permission_request: Optional[P]
            exception: Optional[Exception]
        """
        super().__init__(
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )
