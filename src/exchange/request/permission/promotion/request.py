# src/exchange/request/authorization/promotion.request.py

"""
Module: exchange.request.authorization.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import PermissionRequest, PromotionRequest


class PromotionPermissionRequest(PermissionRequest[PromotionRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides PromotionAuthorizer with a job.

     Attributes:
        id: int
        candidate: PromotionRequest

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int, candidate: PromotionRequest):
        """
        Args:
            id: int
            candidate: PromotionRequest
        """
        super().__init__(id=id, candidate=candidate)
    
    @property
    def candidate(self) -> PromotionRequest:
        return cast(PromotionRequest, super().candidate)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionPermissionRequest):
            return self.id == other.id
        return False