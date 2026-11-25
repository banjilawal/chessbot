# src/artifact/decision/computation/topology/traversal/bishop/request.py

"""
Module: artifact.decision.computation.topology.traversal.bishop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import TraversalTopologyPermissionRequest, BishopTopologyRequest


class BishopTopologyPermissionRequest(
    TraversalTopologyPermissionRequest[BishopTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: BishopTraversalTopologyRequest

     Provides:

     Super Class:
        TraversalTopologyPermissionReques
     """
    
    def __init__(self, id: int, authorization_applicant: BishopTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: BishopTraversalTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> BishopTopologyRequest:
        return cast(BishopTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TraversalTopologyPermissionRequest):
            return self.id == other.id
        return False