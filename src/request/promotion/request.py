# src/request/promotion/request.py

"""
Module: request.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import PawnToken
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

     Provides:
        -   def request(id: int, pawn: PawnToken) -> PromotionRequest:

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

    
    @classmethod
    def request(cls, id: int, pawn: PawnToken) -> PromotionRequest:
        return cls(id=id, pawn=pawn)