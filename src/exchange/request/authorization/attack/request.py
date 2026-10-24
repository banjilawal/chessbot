# src/exchange/request/authorization/encounter.request.py

"""
Module: exchange.request.authorization.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from faulthandler import cancel_dump_traceback_later
from typing import Generic, TypeVar, cast


from domain import Candidate, Token
from exchange import AuthorizationRequest

T = TypeVar("T", bound="Attackequest")

class AttackAuthorizationRequest(AuthorizationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides AttackAuthorizer with a job.

     Attributes:

     Provides:

     Super Class:
        AuthorizationRequest
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
        if isinstance(other, AttackAuthorizationRequest):
            return self.id == other.id
        return False