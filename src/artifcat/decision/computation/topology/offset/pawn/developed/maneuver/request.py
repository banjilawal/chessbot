# src/artifact/decision/computation/topology/offset/pawn/request.py

"""
Module: artifact.decision.computation.topology.offset.pawn.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import DevelopedManeuverTopologyRequest, DevelopedTopologyPermissionRequest


class DevelopedManeuverTopologyPermissionRequest(
    DevelopedTopologyPermissionRequest[DevelopedManeuverTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: DevelopedManeuverTopologyRequest

     Provides:

     Super Class:
        OffsetTopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: DevelopedManeuverTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: DevelopedManeuverTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> DevelopedManeuverTopologyRequest:
        return cast(DevelopedManeuverTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DevelopedManeuverTopologyPermissionRequest):
            return self.id == other.id
        return False