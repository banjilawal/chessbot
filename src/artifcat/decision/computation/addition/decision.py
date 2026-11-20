# src/artifact/decision/computation/add/decision.py

"""
Module: artfifact.decision.computation.add.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import ComputationDecision, Permission
from exchange import VectorAdditionPermissionRequest, VectorAdditionRequest

P = TypeVar("P", bound="VectorAdditionPermissionRequest")
T = TypeVar("T", bound="VectorAdditionRequest")


class VectorAdditionDecision(ComputationDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Computation transaction is permitted.

    Attributes:
        transaction_request: Optional[VectorAdditionRequest]

    Provides:
        -   def grant(
                    transaction_request: VectorAdditionRequest,
                    permission_request: PermissionRequest,
            ) -> AddDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> AddDecision

    Super Class:
        ComputationDecision
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
