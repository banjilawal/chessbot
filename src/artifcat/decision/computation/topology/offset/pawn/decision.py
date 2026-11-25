# src/artifact/decision/computation/topology/offset/pawn/decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import OffsetTopologyDecision, Permission
from request import PawnTopologyPermissionRequest, PawnTopologyRequest

P = TypeVar("P", bound="PawnTopologyPermissionRequest")
T = TypeVar("T", bound="PawnTopologyRequest")

class PawnTopologyDecision(OffsetTopologyDecision[P, T], Generic[P,T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: PawnTopologyRequest
        permission_request: PawnTopologyPermissionRequest
        
    Provides:

    Super Class:
        OffsetTopologyDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[P] | None = None,
            transaction_request: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[PawnTopologyPermissionRequest]
            transaction_request: Optional[PawnTopologyRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
