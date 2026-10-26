# src/exchange/request/permission/promotion.request.py

"""
Module: exchange.request.permission.promotion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import PermissionRequest, PromotionRequest


class PromotionPermissionRequest(
    PermissionRequest[PromotionRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a CrudAuthorizer with job details.

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
    def payload(self) -> PermissionRequest:
        return cast(PromotionRequest, super().payload)
    
    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, PermissionRequest):
            return self.id == other.id
        return False