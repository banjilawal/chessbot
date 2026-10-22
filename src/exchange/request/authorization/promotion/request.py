# src/exchange/request/authorization/promotion.request.py

"""
Module: exchange.request.authorization.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionResult
from domain import Elevatable, PawnToken
from exchange import AuthorizationRequest


class PromotionRequest(AuthorizationRequest[PromotionResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information a PromotionAuthorizer needs to execute a Promotion job.

     Attributes:
        applicant: PawnToken
        activity: Elevatable

     Provides:

     Super Class:
        AuthorizationRequest
     """
    
    def __init__(self, id: int, applicant: PawnToken, activity: Elevatable):
        """
        Args:
            id: int
            applicant: PawnToken
            activity: Elevatable
        """
        super().__init__(id=id, applicant=applicant, activity=activity)
    
    @property
    def applicant(self) -> PawnToken:
        return cast(PawnToken, super().applicant)
    
    @property
    def activity(self) -> Elevatable:
        return cast(Elevatable, super().activity)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionRequest):
            return self.id == other.id
        return False