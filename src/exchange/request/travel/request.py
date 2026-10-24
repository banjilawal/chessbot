# src/exchange/request/travel/request.py

"""
Module: exchange.request.travel.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Path, Token
from exchange import Request

T = TypeVar("T")

class TravelRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a travel job.

     Attributes:
        token: Token
        path: Elevatable

     Provides:
     
     Super Class:
        Request
     """
    _token: Token
    _path: Path
    
    def __init__(
            self,
            id: int,
            token: Token,
            path: Path,
    ):
        """
        Args:
            id: int
            token: Token
            path: Path
        """
        super().__init__(id=id)
        self._token = token
        self._path = path
        
    @property
    def token(self) -> Token:
        return self._token
    
    @property
    def path(self) -> Path:
        return self._path
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TravelRequest):
            return self.id == other.id
        return False