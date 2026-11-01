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
from exchange import CrudPermissionRequest, CrudRequest

P = TypeVar("P", bound="CrudPermissionRequest")
T = TypeVar("T", bound="CrudRequest")


class CrudDecision(Decision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[CrudRequest[T]]

    Provides:
        -   def grant(
                    approval: CrudRequest[T],
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