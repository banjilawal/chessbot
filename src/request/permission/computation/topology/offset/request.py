# src/request/permission/computation/topology/offset/request.py

"""
Module: request.permission.computation.topology.offset.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from request import TopologyPermissionRequest, OffsetTopologyRequest

T = TypeVar("T", bound="OffsetTopologyRequest")

class OffsetTopologyPermissionRequest(
    TopologyPermissionRequest[T], ABC, Generic[T]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides ComputationAuthorizer with a job.

     Attributes:
        id: int
        authorization_applicant: T

     Provides:

     Super Class:
        TopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: T
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OffsetTopologyPermissionRequest):
            return self.id == other.id
        return False