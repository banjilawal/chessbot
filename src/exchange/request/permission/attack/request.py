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
    
    def __init__(self, id: int,  authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: T
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    
    @property
    def authorization_applicant(self) -> T:
        return cast(T, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackPermissionRequest):
            return self.id == other.id
        return False