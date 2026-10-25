# src/exchange/request/transaction/encounter/request.py

"""
Module: exchange.request.transaction.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import AttackResult
from domain import Encounter, Square, Token
from exchange import TransactionRequest

T = TypeVar("T", bound="Encounter")

class AttackRequest(TransactionRequest[AttackResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides AttackWorker with a job.

     Attributes:
        victim: Token
        maneuver_request: Maneuver

     Provides:
     
     Super Class:
        TransactionRequest
     """
    
    _victim: Token
    _location: Square


    
    def __init__(
            self,
            id: int,
            victim: Token,
            location: Square,
    ):
        """
        Args:
            id: int
            victim: Token
            location: Square
        """
        super().__init__(id=id)
        self._victim = victim
        self._location = location
        
    @property
    def location(self) -> Square:
        return self._location
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackRequest):
            return self.id == other.id
        return False