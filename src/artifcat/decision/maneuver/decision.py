# src/artifact/decision/maneuver/decision.py

"""
Module: artfifact.decision.maneuver.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision, Permission
from exchange import PermissionRequest, ManeuverPermissionRequest, ManeuverRequest


class ManeuverDecision(Decision[ManeuverPermissionRequest, ManeuverRequest]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Maneuver transaction is permitted.

    Attributes:
        approval: Optional[ManeuverRequest]

    Provides:
        -   def grant(
                    approval: ManeuverRequest,
                    permission_request: PermissionRequest,
            ) -> ManeuverDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> ManeuverDecision

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[ManeuverRequest] | None = None,
            permission_request: Optional[ManeuverPermissionRequest] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            transaction_request: Optional[ManeuverRequest]
            permission_request: Optional[ManeuverPermissionRequest]
            exception: Optional[Exception]
        """
        super().__init__(
            permission_request=permission_request,
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
        )