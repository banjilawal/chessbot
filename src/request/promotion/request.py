# src/request/promotion/request.py

"""
Module: request.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import PawnToken, Rank
from request import Request


class PromotionRequest(Request):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
        1.  Provide information the PromotionPermitter needs to elevate a pawn's rank.

     Attributes:
         id: int
         pawn: PawnToken
         promotion_level: Rank

     Provides:
        -   def request(id: int, pawn: PawnToken, promotion_level: Rank) -> PromotionRequest:

     Super Class:
        Request
     """
    _candidate: PawnToken
    _promotion_level: Rank
    
    def __init__(self, id: int, candidate: PawnToken, promotion_level: Rank):
        """
         Args:
            id: int
            candidate: PawnToken,
            promotion_level: Rank
        """
        super().__init__(id=id)
        self._candidate = candidate
        self._promotion_level = promotion_level
        
    
    @property
    def candidate(self) -> PawnToken:
        return self._candidate
    
    @property
    def rank_level(self) -> Rank:
        return self._promotion_level

    
    @classmethod
    def request(cls, id: int, candidate: PawnToken, promotion_level: Rank) -> PromotionRequest:
        return cls(id=id, candidate=candidate, promotion_level=promotion_level)