# src/exchange/request/permission/attack/checkmate/request.py

"""
Module: exchange.request.permission.attack.checkmate.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AttackPermissionRequest, CheckmateRequest


class CheckmatePermissionRequest(AttackPermissionRequest[CheckmateRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides CheckmateAuthorizer with a job.

     Attributes:

     Provides:

     Super Class:
        Permission
     """
    
    def __init__(self, id: int,  candidate: CheckmateRequest):
        """
        Args:
            id: int
            candidate: CheckmateRequest
        """
        super().__init__(id=id, candidate=candidate)
    
    
    @property
    def candidate(self) -> CheckmateRequest:
        return cast(CheckmateRequest, super().candidate)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackPermissionRequest):
            return self.id == other.id
        return False