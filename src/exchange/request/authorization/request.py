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
         1. Provide details about a job.

     Attributes:
         id: int
         request: T

     Provides:
     
     Super Class:
     """
    _id: int
    _request: T
    
    def __init__(self, id: int, request: T):
        """
        Args:
            id: int
            request: T
        """
        self._id = id
        self._request = request
        
    @property
    def id(self) -> int:
        return self.id
    
    @property
    def request(self) -> T:
        self._request
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationRequest):
            return self._id == other.id
        return False