# src/exchange/request/transaction/maneuver/request.py

"""
Module: exchange.request.transaction.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar

from artifcat import ManeuverResult
from domain import Maneuver, Path, Token
from exchange import TransactionRequest

R = TypeVar("R", bound="ManeuverResult")
T = TypeVar("T", bound="Maneuver")

class ManeuverRequest(TransactionRequest[R], Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a maneuver job.

     Attributes:
        token: Token
        path: Path
        
     Provides:
     
     Super Class:
        TransactionRequest
     """
    _traveler: Token
    _path: Path
    
    def __init__(
            self,
            id: int,
            traveler: Token,
            path: Path,
    ):
        """
        Args:
            id: int
            traveler: Token
            path: Path
        """
        super().__init__(id=id)
        self._traveler = traveler
        self._path = path
        
    @property
    def traveler(self) -> Token:
        return self._traveler
    
    @property
    def path(self) -> Path:
        return self._path
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverRequest):
            return self.id == other.id
        return False