# src/artifact/decision/computation/topology/offset/king/decision.py

"""
Module: artifact.decision.computation.topology.offset.king.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, OffsetTopologyDecision
from request import KingTopologyPermissionRequest, KingTopologyRequest


class KingTopologyDecision(
    OffsetTopologyDecision[KingTopologyPermissionRequest, KingTopologyRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: KingTopologyRequest
        permission_request: KingTopologyPermissionRequest
        
    Provides:

    Super Class:
        OffsetTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[KingTopologyPermissionRequest] | None = None,
            transaction_request: Optional[KingTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[KingTopologyPermissionRequest]
            transaction_request: Optional[KingTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
