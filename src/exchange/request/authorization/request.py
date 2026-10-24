# src/exchange/request/authorization/request.py

"""
Module: exchange.request.authorization.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


from exchange import Request

T = TypeVar("T", bound="Request")


class AuthorizationRequest(ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information an Authorizer needs to execute a client's job.

     Attributes:
        id: int
        candidate: T

     Provides:
     
     Super Class:
     """
    _id; int
    _candidate: T
    
    def __init__(self, id: int, candidate: T):
        """
        Args:
            id: int
            candidate: T
        """
        self._id = id
        self._candidate = candidate
        
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def candidate(self) -> T:
        return self._candidate

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationRequest):
            return self.id == other.id
        return False