# src/artifact/decision/computation/topology/offset/knight/decision.py

"""
Module: artifact.decision.computation.topology.offset.knight.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Permission, OffsetTopologyDecision
from request import KnightTopologyPermissionRequest, KnightTopologyRequest


class KnightTopologyDecision(
    OffsetTopologyDecision[KnightTopologyPermissionRequest, KnightTopologyRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: KnightTopologyRequest
        permission_request: KnightTopologyPermissionRequest
        
    Provides:

    Super Class:
        OffsetTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[KnightTopologyPermissionRequest] | None = None,
            transaction_request: Optional[KnightTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[KnightTopologyPermissionRequest]
            transaction_request: Optional[KnightTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
