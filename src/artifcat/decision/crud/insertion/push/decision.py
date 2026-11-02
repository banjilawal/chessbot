# src/artifact/decision/crud/insertion/push/decision.py

"""
Module: artfifact.decision.crud.insertion.push.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import InsertionDecision, Permission
from exchange import PushPermissionRequest, ModelPushRequest

P = TypeVar("P", bound="PushPermissionRequest")
T = TypeVar("T", bound="ModelPushRequest")


class PushDecision(InsertionDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Push transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        InsertionDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[P] | None = None,
            transaction_request: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[P]
            transaction_request: Optional[T]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )