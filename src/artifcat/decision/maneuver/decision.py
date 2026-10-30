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


class ManeuverDecision(Decision[ManeuverRequest]):
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
            permission_request: ManeuverPermissionRequest,
            exception: Optional[Exception] | None = None,
            approval: Optional[ManeuverRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            approval: Optional[ManeuverRequest]
        """
        super().__init__(
            permission_request=permission_request,
            approval=approval,
            exception=exception,
            permission=permission,
        )
    
    @property
    def permission_request(self) -> ManeuverPermissionRequest:
        return cast(ManeuverPermissionRequest, super().permission_request)
    
    @property
    def approval(self) -> Optional[ManeuverRequest]:
        return cast(ManeuverRequest, super().approval)
    
    @property
    def request_is_granted(self) -> bool:
        return (
                super().request_is_granted and 
                isinstance(self.approval, ManeuverRequest)
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    
    @classmethod
    def grant(
            cls, 
            approval: ManeuverRequest, 
            permission_request: PermissionRequest,
    ) -> ManeuverDecision:
        role_request = cast(
            ManeuverPermissionRequest, 
            permission_request,
        )
        return cls(
            approval=approval,
            permission_request=role_request,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(
            cls, 
            permission_request: PermissionRequest,
            exception: Exception,
    ) -> ManeuverDecision:
        role_request = cast(
            ManeuverPermissionRequest,
            permission_request,
        )
        return cls(
            exception=exception,
            permission_request=role_request,
            permission=Permission.DENIED,
        )


    
