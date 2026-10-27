# src/exchange/request/validation/context/board/request.py

"""
Module: exchange.request.validation.context.board.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Board
from transit import BoardContextCarrier


class BoardContextValidationRequest(ContextValidationRequest[BoardContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a BoardContextValidator job details.

     Attributes:
         id: int
         item: BoardContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: BoardContextCarrier):
        """
        Args:
            id: int
            item: BoardContextCarrier
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> BoardContextCarrier:
        return cast(BoardContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardContextValidationRequest):
            return self.id == other.id
        return False