# src/artifact/decision/maneuver/decision.py

"""
Module: artfifact.decision.maneuver.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import Decision, Permission
from exchange import ManeuverPermissionRequest, ManeuverRequest

P = TypeVar("P", bound="ManeuverPermissionRequest")
T = TypeVar("T", bound="ManeuverRequest")

class ManeuverDecision(Decision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Maneuver transaction is permitted.

    Attributes:
        transaction_request: Optional[T]
        permission_request: Optional[P]

    Provides:

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[T] | None = None,
            permission_request: Optional[P] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[ManeuverRequest]
            permission_request: Optional[ManeuverPermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
    #
    # @property
    # def transaction_request(self) -> Optional[T]:
    #     return cast(ManeuverRequest, super().transaction_request)
    #
    # @property
    # def permission_request(self) -> Optional[ManeuverPermissionRequest]:
    #     return cast(ManeuverPermissionRequest, super().permission_request)