# src/request/permission/computation/addition/request.py

"""
Module: request.permission.computation.addition.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import ComputationPermissionRequest, VectorAdditionRequest


class VectorAdditionPermissionRequest(ComputationPermissionRequest[VectorAdditionRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: VectorAdditionRequest

     Provides:

     Super Class:
        ComputationPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: VectorAdditionRequest):
        """
        Args:
            id: int
            authorization_applicant: VectorAdditionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> VectorAdditionRequest:
        return cast(VectorAdditionRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorAdditionPermissionRequest):
            return self.id == other.id
        return False