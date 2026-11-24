# src/request/permission/computation/topology/offset/king/request.py

"""
Module: request.permission.computation.topology.offset.king.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import OffsetTopologyPermissionRequest, KingTopologyRequest


class KingTopologyPermissionRequest(
    OffsetTopologyPermissionRequest[KingTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: KingOffsetTopologyRequest

     Provides:

     Super Class:
        OffsetTopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: KingTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: KingOffsetTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> KingTopologyRequest:
        return cast(KingTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OffsetTopologyPermissionRequest):
            return self.id == other.id
        return False