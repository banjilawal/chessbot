# src/request/permission/computation/product/request.py

"""
Module: request.permission.computation.product.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ComputationPermissionRequest, ScalarProductRequest


class ScalarProductPermissionRequest(ComputationPermissionRequest[ScalarProductRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: ScalarProductRequest

     Provides:

     Super Class:
        ScalarProductPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: ScalarProductRequest):
        """
        Args:
            id: int
            authorization_applicant: ScalarProductPermissionRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> ScalarProductRequest:
        return cast(ScalarProductRequest, super().authorization_applicant)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarProductPermissionRequest):
            return self.id == other.id
        return False