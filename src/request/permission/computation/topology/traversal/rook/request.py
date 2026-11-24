# src/request/permission/computation/topology/traversal/rook/request.py

"""
Module: request.permission.computation.topology.traversal.rook.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import TraversalTopologyPermissionRequest, RookTopologyRequest


class RookTopologyPermissionRequest(
    TraversalTopologyPermissionRequest[RookTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: RookTraversalTopologyRequest

     Provides:

     Super Class:
        TraversalTopologyPermissionReques
     """
    
    def __init__(self, id: int, authorization_applicant: RookTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: RookTraversalTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> RookTopologyRequest:
        return cast(RookTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TraversalTopologyPermissionRequest):
            return self.id == other.id
        return False