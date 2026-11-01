# src/artifact/decision/crud/deletion/remove/decision.py

"""
Module: artfifact.decision.crud.deletion.remove.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat.decision.crud.deletion import DeletionDecision
from exchange import RemoveNodePermissionRequest, RemoveNodeRequest

P = TypeVar("P", bound="RemoveNodePermissionRequest")
T = TypeVar("T", bound="RemoveNodeRequest")


class RemoveNodeDecision(DeletionDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[RemoveRequest]

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
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )