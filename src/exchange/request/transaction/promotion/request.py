# src/exchange/request/transaction/promotion/request.py

"""
Module: exchange.request.transaction.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from artifcat import PromotionResult
from domain import Elevatable, PawnToken, Rank
from exchange import TransactionRequest


class PromotionRequest(TransactionRequest[PromotionResult]):
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
        TransactionRequest
     """
    _applicant: PawnToken
    _promotion_level: Rank
    
    def __init__(self, id: int, token: PawnToken, promotion_level: Rank):
        """
        Args:
            id: int
            token: PawnToken
            promotion_level: Rank
        """
        super().__init__(id=id)
        self._applicant = token
        self._promotion_level = promotion_level
        
    @property
    def token(self) -> PawnToken:
        return self._applicant
    
    @property
    def promotion_level(self) -> Rank:
        return self._promotion_level
    
    @property
    def rank_is_elevatable(self) -> bool:
        return isinstance(self._promotion_level, Elevatable)
    
    @property
    def rank_is_not_elevatable(self) -> bool:
        return not self.rank_is_elevatable
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False