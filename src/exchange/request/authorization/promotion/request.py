# src/exchange/request/authorization/promotion.request.py

"""
Module: exchange.request.authorization.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import cast

from artifcat import PromotionResult
from domain import Elevateable, PromotionRequest, Rank
from exchange import AuthorizationRequest, PromotionRequest


class PromotionAuthorizationRequest(AuthorizationRequest[PromotionRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information a PromotionAuthorizer needs to execute a Promotion job.

     Attributes:
        candidate: PromotionRequest
        activity: Elevatable

     Provides:

     Super Class:
        AuthorizationRequest
     """
    
    def __init__(self, id: int, candidate: PromotionRequest):
        """
        Args:
            id: int
            candidate: PromotionRequest
            activity: Elevatable
        """
        super().__init__(id=id, candidate=candidate)
    
    @property
    def candidate(self) -> PromotionRequest:
        return cast(PromotionRequest, super().candidate)
    
    @property
    def activity(self) -> Elevateable:
        return cast(Elevateable, super().activity)
    
    @property
    def activity_to_rank(self) -> Rank:
        return cast(Rank, cast(ABC, self.activity))
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionAuthorizationRequest):
            return self.id == other.id
        return False