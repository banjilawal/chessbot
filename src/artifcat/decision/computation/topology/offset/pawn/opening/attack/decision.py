# src/artifact/decision/computation/topology/offset/pawn/opening/attack/decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.opening.attack.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import OpeningPawnTopologyDecision, Permission
from request import (
    OpeningAttackTopologyPermissionRequest, OpeningAttackTopologyRequest
)


class OpeningAttackTopologyDecision(
    OpeningPawnTopologyDecision[
        OpeningAttackTopologyPermissionRequest,
        OpeningAttackTopologyRequest,
    ]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: OpeningAttackTopologyRequest
        permission_request: OpeningAttackTopologyPermissionRequest
        
    Provides:

    Super Class:
        OpeningPawnTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[OpeningAttackTopologyPermissionRequest] | None = None,
            transaction_request: Optional[OpeningAttackTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[OpeningAttackTopologyPermissionRequest]
            transaction_request: Optional[OpeningAttackTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
