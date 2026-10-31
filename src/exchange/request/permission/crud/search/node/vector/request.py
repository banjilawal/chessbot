# src/exchange/request/permission/crud/search/node/vector/request.py

"""
Module: exchange.request.permission.crud.search.node.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import SearchPermissionRequest, VectorNodeSearchRequest


class VectorNodeSearchPermissionRequest(
    SearchPermissionRequest[VectorNodeSearchRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a VectorNodeSearchPermitter with a job.

     Attributes:
         id: int
         authorization_applicant: : VectorNodeSearchRequest

     Provides:

     Super Class:
        SearchPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: VectorNodeSearchRequest):
        """
        Args:
            id: int
            authorization_applicant: VectorNodeSearchRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> VectorNodeSearchRequest:
        return cast(VectorNodeSearchRequest, super().authorization_applicant)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeSearchPermissionRequest):
            return self.id == other.id
        return False