# src/exchange/request/validation/context/player/request.py

"""
Module: exchange.request.validation.context.player.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Player
from transit import PlayerContextCarrier


class PlayerContextValidationRequest(ContextValidationRequest[PlayerContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a PlayerContextValidator job details.

     Attributes:
         id: int
         item: PlayerContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: PlayerContextCarrier):
        """
        Args:
            id: int
            item: PlayerContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> PlayerContextCarrier:
        return cast(PlayerContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerContextValidationRequest):
            return self.id == other.id
        return False