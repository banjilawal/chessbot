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
from domain import PawnToken, Rank
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
        applicant: PawnToken

     Provides:
     
     Super Class:
        PermissionRequest
     """
    _applicant: PawnToken
    _rank_elevation: Rank
    
    def __init__(
            self,
            id: int,
            applicant: PawnToken,
            rank_elevation: Rank,
    ):
        """
        Args:
            id: int
            applicant: PawnToken
            rank_elevation: Rank
        """
        super().__init__(id=id)
        self._applicant = applicant
        self._rank_elevation = rank_elevation
        
    @property
    def applicant(self) -> PawnToken:
        return self._applicant
    
    @property
    def rank_elevation(self) -> Rank:
        return self._rank_elevation
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False