# src/exchange/request/validation/model/board/request.py

"""
Module: exchange.request.validation.model.board.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelValidationRequest
from domain import Board
from transit import BoardCarrier


class BoardValidationRequest(ModelValidationRequest[Board]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Board a validation job.

     Attributes:
         id: int
         item: BoardCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: BoardCarrier):
        """
        Args:
            id: int
            item: BoardCarrier
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> BoardCarrier:
        return cast(BoardCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardValidationRequest):
            return self.id == other.id
        return False