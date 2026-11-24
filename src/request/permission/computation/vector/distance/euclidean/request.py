# src/request/permission/computation/vector/distance/euclidean/request.py

"""
Module: request.permission.computation.vector.distance.euclidean.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import DistanceVectorComputationPermissionRequest, EuclideanDistanceRequest


class EuclideanDistancePermissionRequest(
    DistanceVectorComputationPermissionRequest[EuclideanDistanceRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: EuclideanDistanceRequest

     Provides:

     Super Class:
        DistanceVectorComputationPermissionReques
     """
    
    def __init__(self, id: int, authorization_applicant: EuclideanDistanceRequest):
        """
        Args:
            id: int
            authorization_applicant: EuclideanDistanceRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> EuclideanDistanceRequest:
        return cast(EuclideanDistanceRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DistanceVectorComputationPermissionRequest):
            return self.id == other.id
        return False