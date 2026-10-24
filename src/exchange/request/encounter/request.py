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

from artifcat import EncounterResult
from domain import Maneuver, Square, Victimizable
from exchange import Request

T = TypeVar("T", bound="Victimizable")

class EncounterRequest(Request[EncounterResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a encounter job.

     Attributes:
        victim: T
        square: Square
        maneuver: Maneuver

     Provides:
     
     Super Class:
        Request
     """
    
    _victim: T
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
            victim: T
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
    def victim(self) -> T:
        return self._victim
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EncounterRequest):
            return self.id == other.id
        return False