# src/exchange/request/permission/crud/deletion/remove/vector/request.py

"""
Module: exchange.request.permission.crud.deletion.remove.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from exchange import RemoveNodePermissionRequest, RemoveVectorNodeRequest


class RemoveVectorNodePermissionRequest(
    RemoveNodePermissionRequest[RemoveVectorNodeRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a RemoveVectorNodePermitter with job details.

     Attributes:
         authorization_applicant: : RemoveVectorNodeRequest

     Provides:

     Super Class:
        RemoveNodePermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: RemoveVectorNodeRequest):
        """
        Args:
            id: int
            authorization_applicant: RemoveVectorNodeRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)