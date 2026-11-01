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
from exchange import PushPermissionRequest, PushRequest

P = TypeVar("P", bound="PushPermissionRequest")
T = TypeVar("T", bound="PushRequest")


class PushDecision(InsertionDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[PushRequest]

    Provides:

    Super Class:
        InsertionDecision
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