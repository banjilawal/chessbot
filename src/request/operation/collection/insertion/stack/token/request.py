# src/request/operation/collection/insertion/stack.token.request.py

"""
Module: request.operation.collection.insertion.stack.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from authorization import StackPushRequest
from collection import TokenStackService
from domain.model import Token


class TokenStackPushRequest(StackPushRequest[Token]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the TokenPush lifecycle

     Attributes:
        id: int
        item: Token
        stack: TokenStackService
        
     Provides:
     
     Super Class:
        PushRequest
     """
    
    def __init__(self, id: int, item: Token, stack: TokenStackService):
        """
        Args:
            id: int
            item: Token
            stack: TokenStackService
        """
        super().__init__(id=id, item=item, stack=stack)
        
    @property
    def item(self) -> Token:
        return cast(Token, super().item)
    
    @property
    def stack(self) -> TokenStackService:
        return cast(TokenStackService, super().stack)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenStackPushRequest):
            request = cast(TokenStackPushRequest, other)
            return self.id == request.id
        return False