# src/request/permission/crud/trim/chain/vector/request.py

"""
Module: request.permission.crud.trim.chain.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from request import ChainTrimPermissionRequest, VectorChainTrimRequest


class VectorChainTrimPermissionRequest(
    ChainTrimPermissionRequest[VectorChainTrimRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a VectorChainTrimPermitter with job details.

     Attributes:
         authorization_applicant: : VectorChainTrimRequest

     Provides:

     Super Class:
        ChainTrimPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: VectorChainTrimRequest):
        """
        Args:
            id: int
            authorization_applicant: VectorChainTrimRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)