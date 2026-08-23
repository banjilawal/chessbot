# src/domain/exchange/request/crud/search/stack/token/request.py

"""
Module: domain.exchange.request.crud.search.stack.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import TokenStackService
from domain import StackSearchRequest, Token, TokenSearchContext


class TokenSearchRequest(StackSearchRequest[Token]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a TokenStackService and criteria a TokenSearcher needs to run a job.

     Attributes:
        id: int
        context: TokenSearchContext
        stack: TokenStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: TokenSearchContext, stack: TokenStackService):
        """
        Args:
            id: int
            context: TokenSearchContext
            stack: TokenStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> TokenSearchContext:
        return cast(TokenSearchContext, super().context)
        
    @property
    def stack(self) -> TokenStackService:
        return cast(TokenStackService, super().stack)
    
    @property
    def collection(self) -> TokenStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False