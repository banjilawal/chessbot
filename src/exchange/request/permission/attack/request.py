# src/exchange/request/permission/encounter.request.py

"""
Module: exchange.request.permission.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast


from exchange import AttackRequest, PermissionRequest

T = TypeVar("T", bound="AttackRequest")

class AttackPermissionRequest(PermissionRequest[T], Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides AttackAuthorizer with a job.

     Attributes:

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int,  candidate: T):
        """
        Args:
            id: int
            candidate: T
        """
        super().__init__(id=id, candidate=candidate)
    
    
    @property
    def candidate(self) -> T:
        return cast(T, super().candidate)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackPermissionRequest):
            return self.id == other.id
        return False