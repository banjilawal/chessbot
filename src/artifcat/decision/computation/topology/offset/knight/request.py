# src/artifact/decision/computation/topology/offset/knight/request.py

"""
Module: artifact.decision.computation.topology.offset.knight.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import OffsetTopologyPermissionRequest, KnightTopologyRequest


class KnightTopologyPermissionRequest(
    OffsetTopologyPermissionRequest[KnightTopologyRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: KnightOffsetTopologyRequest

     Provides:

     Super Class:
        OffsetTopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: KnightTopologyRequest):
        """
        Args:
            id: int
            authorization_applicant: KnightOffsetTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> KnightTopologyRequest:
        return cast(KnightTopologyRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OffsetTopologyPermissionRequest):
            return self.id == other.id
        return False