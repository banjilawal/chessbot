# src/artifact/decision/computation/product/decision.py

"""
Module: artfifact.decision.computation.product.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import ComputationDecision, Permission
from exchange import ScalarProductRequest

P = TypeVar("P", bound="ScalarProductPermissionRequest")
T = TypeVar("T", bound="ScalarProductRequest")


class ScalarProductDecision(ComputationDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Product transaction is permitted.

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