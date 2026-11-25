# src/artifact/decision/computation/topology/offset/pawn/opening/maneuver/decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.opening.maneuver.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import OpeningPawnTopologyDecision, Permission
from request import (
    OpeningManeuverTopologyPermissionRequest, OpeningManeuverTopologyRequest
)


class OpeningManeuverTopologyDecision(
    OpeningPawnTopologyDecision[
        OpeningManeuverTopologyPermissionRequest,
        OpeningManeuverTopologyRequest,
    ]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: OpeningManeuverTopologyRequest
        permission_request: OpeningManeuverTopologyPermissionRequest
        
    Provides:

    Super Class:
        OpeningPawnTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[OpeningManeuverTopologyPermissionRequest] | None = None,
            transaction_request: Optional[OpeningManeuverTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[OpeningManeuverTopologyPermissionRequest]
            transaction_request: Optional[OpeningManeuverTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
