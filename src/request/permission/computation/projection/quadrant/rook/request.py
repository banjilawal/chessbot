# src/request/permission/computation/projection/quadrant/rook/request.py

"""
Module: request.permission.computation.projection.quadrant.rook.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import QuadrantProjectionPermissionRequest, RookProjectionRequest


class RookProjectionPermissionRequest(
    QuadrantProjectionPermissionRequest[RookProjectionRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: RookQuadrantProjectionRequest

     Provides:

     Super Class:
        QuadrantProjectionPermissionReques
     """
    
    def __init__(self, id: int, authorization_applicant: RookProjectionRequest):
        """
        Args:
            id: int
            authorization_applicant: RookQuadrantProjectionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> RookProjectionRequest:
        return cast(RookProjectionRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QuadrantProjectionPermissionRequest):
            return self.id == other.id
        return False