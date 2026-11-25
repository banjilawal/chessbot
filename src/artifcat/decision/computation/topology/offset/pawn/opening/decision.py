# src/artifact/decision/computation/topology/offset/pawn/opening.decision.py

"""
Module: artifact.decision.computation.topology.offset.pawn.opening.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import PawnTopologyDecision, Permission
from request import (
    OpeningPawnTopologyRequest, OpeningTopologyPermissionRequest,
)

P = TypeVar("P", bound="OpeningTopologyPermissionRequest")
T = TypeVar("T", bound="OpeningPawnTopologyRequest")

class OpeningPawnTopologyDecision(PawnTopologyDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:
        transaction_request: T
        permission_request: P
        
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
            permission_request: Optional[P]
            transaction_request: Optional[T]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
