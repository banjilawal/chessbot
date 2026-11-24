# src/request/permission/computation/topology/offset/pawn/request.py

"""
Module: request.permission.computation.topology.offset.pawn.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import OpeningManeuverTopologyRequest, OpeningTopologyPermissionRequest


class OpeningManeuverTopologyPermissionRequest(
    OpeningTopologyPermissionRequest[OpeningManeuverTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: OpeningManeuverTopologyRequest

     Provides:

     Super Class:
        OffsetTopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: OpeningManeuverTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: OpeningManeuverTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> OpeningManeuverTopologyRequest:
        return cast(OpeningManeuverTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OpeningManeuverTopologyPermissionRequest):
            return self.id == other.id
        return False