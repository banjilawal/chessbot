# src/exchange/request/transaction/encounter/kill/request.py

"""
Module: exchange.request.transaction.encounter.kill.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import CombatantToken, KillEncounter, Square
from exchange import AttackRequest, ManeuverRequest


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
    _maneuver_request: ManeuverRequest
    
    def __init__(
            self,
            id: int,
            location: Square,
            maneuver_request: ManeuverRequest,
            victim: CombatantToken,
    ):
        """
        Args:
            id: int
            location: Square
            victim: CombatantToken
            maneuver_request: ManeuverRequest
        """
        super().__init__(id=id, victim=victim, location=location)
        self._maneuver = maneuver_request
    
    @property
    def maneuver_request(self) -> ManeuverRequest:
        return self._maneuver_request
    
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, KillRequest):
            return self.id == other.id
        return False