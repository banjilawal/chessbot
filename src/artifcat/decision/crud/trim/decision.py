# src/artifact/decision/crud/trim/decision.py

"""
Module: artfifact.decision.crud.trim.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import CrudDecision, Permission
from request import TrimPermissionRequest, TrimRequest

P = TypeVar("P", bound="TrimPermissionRequest")
T = TypeVar("T", bound="TrimRequest")


class TrimDecision(CrudDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[TrimRequest]

    Provides:
        -   def grant(
                    transaction_request: TrimRequest,
                    permission_request: PermissionRequest,
            ) -> TrimDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> TrimDecision

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
