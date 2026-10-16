# src/exchange/request/fabrication/model/game/request.py

"""
Module: exchange.request.fabrication.model.game.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Game
from transit import GameCarrier


class GameBuildRequest(ModelBuildRequest[Game]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Game a build job.

     Attributes:
         id: int
         item: GameCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: GameCarrier):
        """
        Args:
            id: int
            item: GameCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> GameCarrier:
        return cast(GameCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameBuildRequest):
            return self.id == other.id
        return False