# src/artifact/decision/attack/decision.py

"""
Module: artfifact.decision.attack.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverDecision, Permission
from exchange import AttackPermissionRequest, AttackRequest


class AttackDecision(ManeuverDecision[AttackPermissionRequest, AttackRequest]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an Attack transaction is permitted.

    Attributes:
        transaction_request: Optional[AttackRequest]
        permission_request: Optional[AttackPermissionRequest]

    Provides:

    Super Class:
        ManeuverDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[AttackRequest] | None = None,
            permission_request: Optional[AttackPermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[AttackRequest]
            permission_request: Optional[AttackPermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
    #
    # @property
    # def transaction_request(self) -> Optional[AttackRequest]:
    #     return cast(AttackRequest, super().transaction_request)
    #
    # @property
    # def permission_request(self) -> Optional[AttackPermissionRequest]:
    #     return cast(AttackPermissionRequest, super().permission_request)