# src/request/microservice/token/promotion/request.py

"""
Module: request.microservice.token.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from authorization import TokenServiceRequest
from domain.model import PawnToken, Rank



class PromotionRequest(TokenServiceRequest):
    """
     Role:
         -  Messaging
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
    
    
    def __init__(self, id: int, candidate: PawnToken, promotion_level: Rank, microservice: TokenService):
        """
         Args:
            id: int
            candidate: PawnToken,
            promotion_level: Rank
        """
        super().__init__(id=id, microservice=microservice)
        self._candidate = candidate
        self._promotion_level = promotion_level
        
    
    @property
    def candidate(self) -> PawnToken:
        return self._candidate
    
    @property
    def rank_level(self) -> Rank:
        return self._promotion_level