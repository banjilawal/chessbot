# src/exchange/request/permission/promotion/request.py

"""
Module: exchange.request.permission.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import TypeVar

from artifcat import PromotionResult
from domain import PawnToken
from exchange import PermissionRequest

T = TypeVar("T")

class PromotionRequest(PermissionRequest[PromotionResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a promotion job.

     Attributes:
         id: int
         candidate_pawn: PawnToken

     Provides:
     
     Super Class:
        PermissionRequest
     """
    candidate_pawn: PawnToken
    
    def __init__(self, id: int, candidate_pawn: PawnToken):
        """
        Args:
            id: int
            candidate_pawn: PawnToken
        """
        super().__init__(id=id)
        self._candidate_pawn = candidate_pawn
        
    @property
    def candidate_pawn(self) -> PawnToken:
        return self._candidate_pawn
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False