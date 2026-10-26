# src/exchange/request/permission/attack/warning/request.py

"""
Module: exchange.request.permission.attack.warning.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AttackPermissionRequest, WarningRequest


class WarningPermissionRequest(AttackPermissionRequest[WarningRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides WarningAuthorizer with a job.

     Attributes:

     Provides:

     Super Class:
        Permission
     """
    
    def __init__(self, id: int,  candidate: WarningRequest):
        """
        Args:
            id: int
            candidate: WarningRequest
        """
        super().__init__(id=id, candidate=candidate)
    
    
    @property
    def payload(self) -> WarningRequest:
        return cast(WarningRequest, super().payload)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackPermissionRequest):
            return self.id == other.id
        return False