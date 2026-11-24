# src/request/permission/computation/sequence/sequence/request.py

"""
Module: request.permission.computation.sequence.sequence.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from request import ComputationPermissionRequest, VectorNodeSequenceRequest


class VectorNodeSequencePermissionRequest(
    ComputationPermissionRequest[VectorNodeSequenceRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: VectorNodeSequenceRequest

     Provides:

     Super Class:
        ComputationPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: VectorNodeSequenceRequest):
        """
        Args:
            id: int
            authorization_applicant: VectorNodeSequenceRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
        
    @property
    def authorization_applicant(self) -> VectorNodeSequenceRequest:
        return cast(VectorNodeSequenceRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeSequencePermissionRequest):
            return self.id == other.id
        return False