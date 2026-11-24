# src/request/permission/computation/projection/axis/north/request.py

"""
Module: request.permission.computation.projection.axis.north.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import AxisProjectionPermissionRequest, NorthAxisProjectionRequest


class NorthAxisProjectionPermissionRequest(
    AxisProjectionPermissionRequest[NorthAxisProjectionRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: NorthAxisAxisProjectionRequest

     Provides:

     Super Class:
        AxisProjectionPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: NorthAxisProjectionRequest):
        """
        Args:
            id: int
            authorization_applicant: NorthAxisAxisProjectionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> NorthAxisProjectionRequest:
        return cast(NorthAxisProjectionRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AxisProjectionPermissionRequest):
            return self.id == other.id
        return False