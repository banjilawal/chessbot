# src/exchange/request/promotion/request.py

"""
Module: exchange.request.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import PromotionResult
from domain import Elevateable, PawnToken
from exchange import Request

class PromotionRequest(Request[PromotionResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a promotion job.

     Attributes:
        pawn_token: PawnToken
        rank_elevation: Elevatable

     Provides:
     
     Super Class:
        Request
     """
    _pawn_token: PawnToken
    _rank_elevation: Elevateable
    
    def __init__(
            self,
            id: int,
            pawn_token: PawnToken,
            rank_elevation: Elevateable,
    ):
        """
        Args:
            id: int
            pawn_token: PawnToken
            rank_elevation: Elevateable
        """
        super().__init__(id=id)
        self._pawn_token = pawn_token
        self._rank_elevation = rank_elevation
        
    @property
    def pawn_token(self) -> PawnToken:
        return self._pawn_token
    
    @property
    def rank_elevation(self) -> Elevateable:
        return self._rank_elevation
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False