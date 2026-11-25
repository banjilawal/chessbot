# src/artifact/decision/computation/vector/distance/decision.py

"""
Module: artfifact.decision.computation.vector.distance.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Self, TypeVar

from artifcat import VectorComputationDecision, Permission
from exchange import DistanceComputationPermissionRequest, EuclideanDistanceRequest

P = TypeVar("P", bound="DistanceComputationPermissionRequest")
T = TypeVar("T", bound="EuclideanDistanceRequest")


class DistanceVectorComputationDecision(VectorComputationDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an Distance transaction is permitted.

    Attributes:
    
    Provides:
        -   def do_nothing() -> DistanceDecision
        
    Super Class:
        VectorComputationDecision
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
        
    @classmethod
    def do_nothing(cls) -> Self:
        return cls(permission=Permission.DO_NOTHING)
