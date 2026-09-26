# src/client/request/validation/model/arena/request.py

"""
Module: client.request.validation.model.arena.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from client import ModelValidationRequest
from domain import Arena
from transit import ArenaCarrier


class ArenaValidationRequest(ModelValidationRequest[Arena]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Arena a validation job.

     Attributes:
         id: int
         item: ArenaCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: ArenaCarrier):
        """
        Args:
            id: int
            item: ArenaCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> ArenaCarrier:
        return cast(ArenaCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaValidationRequest):
            return self.id == other.id
        return False