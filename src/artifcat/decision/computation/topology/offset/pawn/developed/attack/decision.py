# src/artifact/decision/computation/topology/offset/pawn/developed/attack/decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.developed.attack.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import DevelopedPawnTopologyDecision, Permission
from request import (
    DevelopedAttackTopologyPermissionRequest, DevelopedAttackTopologyRequest
)


class DevelopedAttackTopologyDecision(
    DevelopedPawnTopologyDecision[
        DevelopedAttackTopologyPermissionRequest,
        DevelopedAttackTopologyRequest,
    ]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: DevelopedAttackTopologyRequest
        permission_request: DevelopedAttackTopologyPermissionRequest
        
    Provides:

    Super Class:
        DevelopedPawnTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[DevelopedAttackTopologyPermissionRequest] | None = None,
            transaction_request: Optional[DevelopedAttackTopologyRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[DevelopedAttackTopologyPermissionRequest]
            transaction_request: Optional[DevelopedAttackTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
