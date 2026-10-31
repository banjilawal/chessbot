# src/exchange/request/permission/crud/insertion/add/vector/request.py

"""
Module: exchange.request.permission.crud.insertion.add.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AddNodePermissionRequest, AddVectorNodeRequest


class AddVectorNodePermissionRequest(
    AddNodePermissionRequest[AddVectorNodeRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides an AddVectorNodePermitter with job details.

     Attributes:
         id: int
         authorization_applicant: : AddVectorNodeRequest

     Provides:

     Super Class:
        AddNodePermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: AddVectorNodeRequest):
        """
        Args:
            id: int
            authorization_applicant: AddVectorNodeRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> AddVectorNodeRequest:
        return cast(AddVectorNodeRequest, super().authorization_applicant)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddVectorNodePermissionRequest):
            return self.id == other.id
        return False