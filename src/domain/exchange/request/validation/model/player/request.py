# src/domain/exchange/request/validation/model/player/request.py

"""
Module: domain.exchange.request.validation.model.player.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Player
from transit import PlayerCarrier


class PlayerValidationRequest(ModelValidationRequest[Player]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a PlayerValidator.

     Attributes:
         id: int
         item: PlayerCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
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
        if isinstance(other, PlayerValidationRequest):
            return self.id == other.id
        return False