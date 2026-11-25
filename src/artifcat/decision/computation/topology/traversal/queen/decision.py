# src/artifact/decision/computation/topology/traversal/queen/decision.py

"""
Module: artifact.decision.computation.topology.traversal.queen.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, TraversalTopologyDecision
from request import QueenTopologyPermissionRequest, QueenTopologyRequest


class QueenTopologyDecision(
    TraversalTopologyDecision[QueenTopologyPermissionRequest, QueenTopologyRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: QueenTopologyRequest
        permission_request: QueenTopologyPermissionRequest
        
    Provides:

    Super Class:
        TraversalTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[QueenTopologyPermissionRequest] | None = None,
            transaction_request: Optional[QueenTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[QueenTopologyPermissionRequest]
            transaction_request: Optional[QueenTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
