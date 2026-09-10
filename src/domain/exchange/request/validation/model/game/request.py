# src/domain/exchange/request/validation/model/game/request.py

"""
Module: domain.exchange.request.validation.model.game.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Game
from transit import GameCarrier


class GameValidationRequest(ModelValidationRequest[Game]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a GameValidator.

     Attributes:
         id: int
         item: GameCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
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
        if isinstance(other, GameValidationRequest):
            return self.id == other.id
        return False