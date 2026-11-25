# src/artifact/decision/computation/topology/traversal/request.py

"""
Module: artifact.decision.computation.topology.traversal.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import Permission, TopologyComputationDecision
from request import TraversalTopologyPermissionRequest, TraversalTopologyRequest

P = TypeVar("P", bound="TraversalTopologyPermissionRequest")
T = TypeVar("T", bound="TraversalTopologyRequest")

class TraversalTopologyDecision(TopologyComputationDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a TopologyComputation transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        ComputationDecision
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