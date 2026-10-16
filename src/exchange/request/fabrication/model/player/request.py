# src/exchange/request/fabrication/model/player/request.py

"""
Module: exchange.request.fabrication.model.player.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Player
from transit import PlayerCarrier


class PlayerBuildRequest(ModelBuildRequest[Player]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Player a build job.

     Attributes:
         id: int
         item: PlayerCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: PlayerCarrier):
        """
        Args:
            id: int
            item: PlayerCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> PlayerCarrier:
        return cast(PlayerCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerBuildRequest):
            return self.id == other.id
        return False