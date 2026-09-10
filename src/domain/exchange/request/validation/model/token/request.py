# src/domain/exchange/request/validation/model/token/request.py

"""
Module: domain.exchange.request.validation.model.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Token
from transit import TokenCarrier


class TokenValidationRequest(ModelValidationRequest[Token]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a TokenValidator.

     Attributes:
         id: int
         item: TokenCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: TokenCarrier):
        """
        Args:
            id: int
            item: TokenCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> TokenCarrier:
        return cast(TokenCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenValidationRequest):
            return self.id == other.id
        return False