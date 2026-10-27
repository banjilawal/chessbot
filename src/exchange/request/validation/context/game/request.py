# src/exchange/request/validation/context/game/request.py

"""
Module: exchange.request.validation.context.game.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Game
from transit import GameContextCarrier


class GameContextValidationRequest(ContextValidationRequest[GameContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a GameContextValidator job details.

     Attributes:
         id: int
         item: GameContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: GameContextCarrier):
        """
        Args:
            id: int
            item: GameContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> GameContextCarrier:
        return cast(GameContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameContextValidationRequest):
            return self.id == other.id
        return False