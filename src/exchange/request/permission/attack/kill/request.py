# src/exchange/request/permission/attack/kill/request.py

"""
Module: exchange.request.permission.attack.kill.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AttackPermissionRequest, KillRequest


class KillPermissionRequest(AttackPermissionRequest[KillRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides KillAuthorizer with a job.

     Attributes:

     Provides:

     Super Class:
        Permission
     """
    
    def __init__(self, id: int,  authorization_applicant: KillRequest):
        """
        Args:
            id: int
            authorization_applicant: KillRequest
        """
        super().__init__(id=id, authorization_applicant=authorization_applicant)
    
    
    @property
    def authorization_applicant(self) -> KillRequest:
        return cast(KillRequest, super().authorization_applicant)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackPermissionRequest):
            return self.id == other.id
        return False