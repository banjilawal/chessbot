# src/request/permission/computation/distance/request.py

"""
Module: request.permission.computation.distance.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ComputationPermissionRequest, EuclideanDistanceRequest


class DistanceComputationPermissionRequest(ComputationPermissionRequest[EuclideanDistanceRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: DistanceComputationRequest

     Provides:

     Super Class:
        DistancePermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: EuclideanDistanceRequest):
        """
        Args:
            id: int
            authorization_applicant: DistanceComputationRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> EuclideanDistanceRequest:
        return cast(EuclideanDistanceRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DistanceComputationPermissionRequest):
            return self.id == other.id
        return False