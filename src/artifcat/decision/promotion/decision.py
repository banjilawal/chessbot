# src/artifact/decision/promotion/decision.py

"""
Module: artfifact.decision.promotion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import Decision, Permission
from exchange import PromotionPermissionRequest, PromotionRequest


class PromotionDecision(Decision[PromotionPermissionRequest, PromotionRequest]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Promotion transaction is permitted.

    Attributes:
        permission_request: Optional[PermissionRequest]
        transaction_request: Optional[PromotionRequest]

    Provides:

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[PromotionRequest] | None = None,
            permission_request: Optional[PromotionPermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[PermissionRequest]
            transaction_request: Optional[PromotionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,

        )

    
