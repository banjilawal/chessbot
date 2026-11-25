# src/artifact/decision/computation/vector/multiplication/decision.py

"""
Module: artfifact.decision.computation.vector.multiplication.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, VectorComputationDecision
from request import ScalarProductPermissionRequest, ScalarProductRequest


class ScalarProductDecision(
    VectorComputationDecision[ScalarProductPermissionRequest, ScalarProductRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Product transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        VectorComputationDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[ScalarProductPermissionRequest] | None = None,
            transaction_request: Optional[ScalarProductRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[ScalarProductPermissionRequest]
            transaction_request: Optional[ScalarProductRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )