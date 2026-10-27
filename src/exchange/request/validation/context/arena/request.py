# src/exchange/request/validation/context/arena/request.py

"""
Module: exchange.request.validation.context.arena.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Arena, ArenaContext
from transit import ArenaContextCarrier


class ArenaContextValidationRequest(ContextValidationRequest[ArenaContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a ArenaContextValidator job details.

     Attributes:
         id: int
         item: ArenaContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: ArenaContextCarrier):
        """
        Args:
            id: int
            item: ArenaContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> ArenaContextCarrier:
        return cast(ArenaContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaContextValidationRequest):
            return self.id == other.id
        return False