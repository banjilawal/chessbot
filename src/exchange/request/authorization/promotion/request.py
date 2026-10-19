# src/exchange/request/authorization/promotion/request.py

"""
Module: exchange.request.authorization.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AuthorizationRequest, PromotionRequest


class PromotionAuthorizationRequest(AuthorizationRequest[PromotionRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a PromotionRequest that needs to be reviewed before it
            the operation can proceed.

     Attributes:
         id: int
         request: PromotionRequest

     Provides:
     
     Super Class:
        AuthorizationRequest
     """
    
    def __init__(self, id: int, request: PromotionRequest):
        """
        Args:
            id: int
            request: PromotionRequest
        """
        super().__init__(id=id, request=request)
    
    @property
    def request(self) -> PromotionRequest:
        return cast(PromotionRequest, super().request)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionAuthorizationRequest):
            return self.id == other.id
        return False