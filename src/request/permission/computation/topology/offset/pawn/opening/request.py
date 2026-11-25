# src/request/permission/computation/topology/offset/pawn/request.py

"""
Module: request.permission.computation.topology.offset.pawn.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from request import (
    OpeningPawnTopologyRequest, PawnTopologyPermissionRequest,
)

T = TypeVar("T", bound="OpeningPawnTopologyRequest")

class OpeningTopologyPermissionRequest(PawnTopologyPermissionRequest[T], ABC, Generic[T]):
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
        OffsetTopologyPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: PawnOffsetTopologyRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OpeningTopologyPermissionRequest):
            return self.id == other.id
        return False