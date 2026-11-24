# src/request/permission/computation/projection/axis/eastAxis/request.py

"""
Module: request.permission.computation.projection.axis.eastAxis.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import AxisProjectionPermissionRequest, EastAxisProjectionRequest


class EastAxisProjectionPermissionRequest(
    AxisProjectionPermissionRequest[EastAxisProjectionRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: EastAxisAxisProjectionRequest

     Provides:

     Super Class:
        AxisProjectionPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: EastAxisProjectionRequest):
        """
        Args:
            id: int
            authorization_applicant: EastAxisAxisProjectionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> EastAxisProjectionRequest:
        return cast(EastAxisProjectionRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AxisProjectionPermissionRequest):
            return self.id == other.id
        return False