# src/artifact/decision/crud/trim/chain/vector/decision.py

"""
Module: artfifact.decision.crud.trim.chain.vector.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import ChainTrimDecision, Permission
from request import VectorChainTrimPermissionRequest, VectorChainTrimRequest


class VectorChainTrimDecision(
    ChainTrimDecision[VectorChainTrimPermissionRequest, VectorChainTrimRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[ChainRequest]

    Provides:

    Super Class:
        ChainTrimDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[VectorChainTrimRequest] | None = None,
            permission_request: Optional[VectorChainTrimPermissionRequest] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            transaction_request: Optional[VectorChainTrimRequest]
            permission_request: Optional[VectorChainTrimPermissionRequest]
            exception: Optional[Exception]
        """
        super().__init__(
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )