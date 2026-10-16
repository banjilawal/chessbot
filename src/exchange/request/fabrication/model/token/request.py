# src/exchange/request/fabrication/model/token/request.py

"""
Module: exchange.request.fabrication.model.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Token
from transit import TokenCarrier


class TokenBuildRequest(ModelBuildRequest[Token]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Token a build job.

     Attributes:
         id: int
         item: TokenCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
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
        if isinstance(other, TokenBuildRequest):
            return self.id == other.id
        return False