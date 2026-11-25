# src/artifact/decision/computation/vector/distance/decision.py

"""
Module: artfifact.decision.computation.vector.distance.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from artifcat import VectorComputationDecision, Permission
from request import DistancePermissionRequest, DistanceRequest


class DistanceComputationDecision(
    VectorComputationDecision[DistancePermissionRequest, DistanceRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an Distance transaction is permitted.

    Attributes:
    
    Provides:
        -   def do_nothing() -> DistanceDecision
        
    Super Class:
        VectorComputationDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[DistancePermissionRequest] | None = None,
            transaction_request: Optional[DistanceRequest] | None = None,
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
