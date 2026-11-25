# src/artifact/decision/computation/sequence/decision.py

"""
Module: artfifact.decision.computation.sequence.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import ComputationDecision, Permission
from request import VectorNodeSequencePermissionRequest, VectorNodeSequenceRequest


class SequenceComputationDecision(
    ComputationDecision[VectorNodeSequencePermissionRequest, VectorNodeSequenceRequest]
):
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
            permission_request: Optional[VectorNodeSequencePermissionRequest] | None = None,
            transaction_request: Optional[VectorNodeSequenceRequest] | None = None,
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