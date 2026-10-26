# src/exchange/request/permission/maneuver.request.py

"""
Module: exchange.request.permission.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import PermissionRequest, ManeuverRequest


class ManeuverPermissionRequest(PermissionRequest[ManeuverRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ManeuverAuthorizer with a job.

     Attributes:
        id: int
        candidate: ManeuverRequest

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int, candidate: ManeuverRequest):
        """
        Args:
            id: int
            candidate: ManeuverRequest
        """
        super().__init__(id=id, candidate=candidate)
    
    @property
    def payload(self) -> ManeuverRequest:
        return cast(ManeuverRequest, super().payload)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverPermissionRequest):
            return self.id == other.id
        return False