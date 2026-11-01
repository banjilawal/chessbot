# src/artifact/decision/crud/deletion/pop/decision.py

"""
Module: artfifact.decision.crud.deletion.pop.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import DeletionDecision, Permission
from exchange import PopPermissionRequest, PopRequest

P = TypeVar("P", bound="PopPermissionRequest")
T = TypeVar("T", bound="PopRequest")


class PopDecision(DeletionDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[PopRequest]

    Provides:

    Super Class:
        DeletionDecision
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
            approval=approval,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )