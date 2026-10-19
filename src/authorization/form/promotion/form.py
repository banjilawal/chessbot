# src/authorization/form/promotion/form.py

"""
Module: authorization.form.promotion.form
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from authorization.form import AuthorizationForm
from exchange import PromotionRequest


class PromotionAuthorizationForm(AuthorizationForm[PromotionRequest]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a PromotionRequest that needs to be reviewed before it
            the operation can proceed.

     Attributes:
         id: int
         operation: PromotionRequest

     Provides:
     
     Super Class:
        AuthorizationForm
     """
    
    def __init__(self, id: int, operation: PromotionRequest):
        """
        Args:
            id: int
            operation: PromotionRequest
        """
        super().__init__(id=id, operation=operation)
    
    @property
    def operation(self) -> PromotionRequest:
        return cast(PromotionRequest, super().operation)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PromotionAuthorizationForm):
            return self.id == other.id
        return False