# src/exchange/request/promotion/request.py

"""
Module: exchange.request.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import cast

from artifcat import PromotionResult
from domain import Elevatable, PawnToken, Rank
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
    _applicant: PawnToken
    _elevatable: Elevatable
    
    def __init__(self, id: int, applicant: PawnToken, elevatable: Elevatable):
        """
        Args:
            id: int
            applicant: PawnToken
            elevatable: Elevatable
        """
        super().__init__(id=id)
        self._applicant = applicant
        self._elevatable = elevatable
        
    @property
    def applicant(self) -> PawnToken:
        return self._applicant
    
    @property
    def elevatable(self) -> Elevatable:
        return self._elevatable
    
    @property
    def elevatable_to_rank(self) -> Rank:
        return cast(Rank, cast(ABC, self._elevatable))
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False