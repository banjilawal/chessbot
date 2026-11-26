# src/artifact/decision/computation/projection/axis/decision.py

"""
Module: artfifact.decision.computation.projection.axis.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, ProjectionDecision
from request import AxisProjectionPermissionRequest, AxisProjectionRequest


class AxisProjectionDecision(
    ProjectionDecision[AxisProjectionPermissionRequest, AxisProjectionRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Computation transaction is permitted.

    Attributes:
        transaction_request: Optional[AxisProjectionRequest]
        permission_request: Optional[AxisProjectionPermissionRequest]
        
    Provides:

    Super Class:
        ProjectionComputationDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[AxisProjectionPermissionRequest] | None = None,
            transaction_request: Optional[AxisProjectionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[AxisProjectionPermissionRequest]
            transaction_request: Optional[AxisProjectionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )