# src/artifact/decision/computation/decision.py

"""
Module: artfifact.decision.computation.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Self, TypeVar

from artifcat import Decision, Permission
from exchange import ComputationPermissionRequest, ComputationRequest

P = TypeVar("P", bound="ComputationPermissionRequest")
T = TypeVar("T", bound="ComputationRequest")


class ComputationDecision(Decision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Computation transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        Decision
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