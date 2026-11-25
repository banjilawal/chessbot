# src/artifact/decision/computation/vector/add/decision.py

"""
Module: artfifact.decision.computation.vector.add.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import VectorComputationDecision, Permission
from request import VectorAdditionPermissionRequest, VectorAdditionRequest


class VectorAdditionDecision(
    VectorComputationDecision[VectorAdditionPermissionRequest, VectorAdditionRequest]
):
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
        VectorComputationDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[VectorAdditionRequest] | None = None,
            permission_request: Optional[VectorAdditionPermissionRequest] | None = None,
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
