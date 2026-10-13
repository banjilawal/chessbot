# src/exchange/request/validation/struct/binder/player/request.py

"""
Module: exchange.request.validation.struct.binder.player.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import PlayerBinder
from exchange import BinderValidationRequest
from transit import PlayerBinderCarrier


class PlayerBinderValidationRequest(
    BinderValidationRequest[PlayerBinder]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a PlayerBinderValidator
            needs to run a job.

     Attributes:
         id: int
         item: BinderCarrier[T]

     Provides:
     
     Super Class:
        BinderValidationRequest
     """
    
    def __init__(self, id: int, item: PlayerBinderCarrier):
        """
        Args:
            id: int
            item: PlayerBinderCarrier
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> PlayerBinderCarrier:
        return cast(PlayerBinderCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BinderValidationRequest):
            return self.id == other.id
        return False