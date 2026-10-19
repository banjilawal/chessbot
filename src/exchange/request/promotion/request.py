# src/exchange/request/promotion/request.py

"""
Module: exchange.request.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import TypeVar

from artifcat import PromotionResult
from domain import PawnToken
from exchange import Request

T = TypeVar("T")

class PromotionRequest(Request[PromotionResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a promotion job.

     Attributes:
         id: int
         pawn: PawnToken

     Provides:
     
     Super Class:
        Request
     """
    _pawn: PawnToken
    
    def __init__(self, id: int, pawn: PawnToken):
        """
        Args:
            id: int
            pawn: PawnToken
        """
        super().__init__(id=id)
        self._pawn = pawn
        
    @property
    def pawn(self) -> PawnToken:
        return self._pawn
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False