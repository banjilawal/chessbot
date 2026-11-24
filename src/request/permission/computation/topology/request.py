# src/request/permission/computation/topology/topology/request.py

"""
Module: request.permission.computation.topology.topology.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic
from typing_extensions import TypeVar

from request import ComputationPermissionRequest, TopologyRequest

T = TypeVar("T", bound="TopologyRequest")

class TopologyPermissionRequest(ComputationPermissionRequest[T], ABC, Generic[T]):
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
        if isinstance(other, TopologyPermissionRequest):
            return self.id == other.id
        return False