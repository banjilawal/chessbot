# src/exchange/request/encounter/request.py

"""
Module: exchange.request.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import AttackResult
from domain import Maneuver, Square, Token
from exchange import Request

T = TypeVar("T", bound="AttackResult")

class AttackRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides AttackWorker with a job.

     Attributes:
        victim: Token
        maneuver: Maneuver

     Provides:
     
     Super Class:
        Request
     """
    
    _victim: Token
    _location: Square
    _maneuver: Maneuver

    
    def __init__(
            self,
            id: int,
            victim: T,
            location: Square,
            maneuver: Maneuver,
    ):
        """
        Args:
            id: int
            victim: Token
            location: Square
            maneuver: Maneuver
        """
        super().__init__(id=id)
        self._victim = victim
        self._location = location
        self._maneuver = maneuver
        
    @property
    def square(self) -> Square:
        return self._location
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackRequest):
            return self.id == other.id
        return False