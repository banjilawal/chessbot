# src/exchange/request/encounter/kill/request.py

"""
Module: exchange.request.encounter.kill.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import KillEncounter, Maneuver, Square
from exchange import AttackRequest


class KillRequest(AttackRequest[KillEncounter]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an encounter job.

     Attributes:
        square: Square
        maneuver: Maneuver
        victim: KillEncounter

     Provides:
     
     Super Class:
        Request
     """
    
    def __init__(
            self,
            id: int,
            location: Square,
            maneuver: Maneuver,
            victim: KillEncounter,
    ):
        """
        Args:
            id: int
            location: Square
            maneuver: Maneuver
            victim: KillEncounter
        """
        super().__init__(
            id=id,
            victim=victim,
            location=location,
            maneuver=maneuver
        )

    @property
    def square(self) -> Square:
        return self._location
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def victim(self) -> KillEncounter:
        return cast(KillEncounter, super().victim)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, KillRequest):
            return self.id == other.id
        return False