# src/artifact/decision/computation/projection/quadrant/decision.py

"""
Module: artfifact.decision.computation.projection.quadrant.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, ProjectionDecision
from request import QuadrantProjectionPermissionRequest, QuadrantProjectionRequest


class QuadrantProjectionDecision(
    ProjectionDecision[QuadrantProjectionPermissionRequest, QuadrantProjectionRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Computation transaction is permitted.

    Attributes:
        transaction_request: Optional[QuadrantProjectionRequest]
        permission_request: Optional[QuadrantProjectionPermissionRequest]
        
    Provides:

    Super Class:
        ProjectionComputationDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[QuadrantProjectionPermissionRequest] | None = None,
            transaction_request: Optional[QuadrantProjectionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[QuadrantProjectionPermissionRequest]
            transaction_request: Optional[QuadrantProjectionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )