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
         promoted_rank: Rank

     Provides:
        -   def request(id: int, pawn: PawnToken, promoted_rank: Rank) -> PromotionRequest:

     Super Class:
        Request
     """
    _pawn: PawnToken
    _promoted_rank: Rank
    
    def __init__(self, id: int, pawn: PawnToken, promoted_rank: Rank):
        """
         Args:
            id: int
            pawn: PawnToken,
            promoted_rank: Rank
        """
        super().__init__(id=id)
        self._pawn = pawn
        self._promoted_rank = promoted_rank
        
    
    @property
    def candidate(self) -> PawnToken:
        return self._pawn
    
    @property
    def rank_level(self) -> Rank:
        return self._promoted_rank

    
    @classmethod
    def request(cls, id: int, pawn: PawnToken, promoted_rank: Rank) -> PromotionRequest:
        return cls(id=id, pawn=pawn, promoted_rank=promoted_rank)