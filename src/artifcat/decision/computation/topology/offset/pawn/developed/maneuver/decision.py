# src/artifact/decision/computation/topology/offset/pawn/developed/maneuver/decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.developed.maneuver.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import DevelopedPawnTopologyDecision, Permission
from request import (
    DevelopedManeuverTopologyPermissionRequest, DevelopedManeuverTopologyRequest
)


class DevelopedManeuverTopologyDecision(
    DevelopedPawnTopologyDecision[
        DevelopedManeuverTopologyPermissionRequest,
        DevelopedManeuverTopologyRequest,
    ]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: DevelopedManeuverTopologyRequest
        permission_request: DevelopedManeuverTopologyPermissionRequest
        
    Provides:

    Super Class:
        DevelopedPawnTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[DevelopedManeuverTopologyPermissionRequest] | None = None,
            transaction_request: Optional[DevelopedManeuverTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[DevelopedManeuverTopologyPermissionRequest]
            transaction_request: Optional[DevelopedManeuverTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
