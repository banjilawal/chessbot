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
        authorization_applicant: ManeuverRequest

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: ManeuverRequest):
        """
        Args:
            id: int
            authorization_applicant: ManeuverRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> ManeuverRequest:
        return cast(ManeuverRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverPermissionRequest):
            return self.id == other.id
        return False