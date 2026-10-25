# src/exchange/request/transaction/encounter/warning/request.py

"""
Module: exchange.request.transaction.encounter.warning.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import EncounterWarning, KingToken, Maneuver, Square, Token
from exchange import AttackRequest

class WarningRequest(AttackRequest[EncounterWarning]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an encounter job.

     Attributes:
        square: Square
        maneuver: Maneuver
        victim: KingToken

     Provides:
     
     Super Class:
        Request
     """
    _enemy: Token
    _enemy_origin: Square
    
    def __init__(
            self,
            id: int,
            enemy: Token,
            checked_king: KingToken,
            enemy_origin: Square,
            location: Square
    ):
        """
        Args:
            id: int
            enemy: Token,
            checked_king: KingToken
            location: Square
            enemy_origin: Square
        """
        super().__init__(
            id=id,
            victim=checked_king,
            location=location,
        )
        self._enemy = enemy
        self._enemy_origin = enemy_origin
    
    @property
    def checked_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.checked_king
    
    @property
    def enemy(self) -> Token:
        return self._enemy
    
    @property
    def enemy_origin(self) -> Square:
        return self._enemy_origin
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, WarningRequest):
            return self.id == other.id
        return False