# src/request/permission/computation/projection/quadrant/bishop/request.py

"""
Module: request.permission.computation.projection.quadrant.bishop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import QuadrantProjectionPermissionRequest, BishopProjectionRequest


class BishopProjectionPermissionRequest(
    QuadrantProjectionPermissionRequest[BishopProjectionRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: BishopQuadrantProjectionRequest

     Provides:

     Super Class:
        QuadrantProjectionPermissionReques
     """
    
    def __init__(self, id: int, authorization_applicant: BishopProjectionRequest):
        """
        Args:
            id: int
            authorization_applicant: BishopQuadrantProjectionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> BishopProjectionRequest:
        return cast(BishopProjectionRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QuadrantProjectionPermissionRequest):
            return self.id == other.id
        return False