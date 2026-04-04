# src/logic/token/database/search/context/context.py

"""
Module: logic.token.database.search.context.context
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import List, TypeVar

from logic.system import StackQuery
from logic.token import Token, TokenContext

T = TypeVar("T")


class TokenQuery(StackQuery[Token]):
    
    def __init__(self, stack: List[Token], context: TokenContext):
        """
        Args:
            stack: List[Token]
            context: TokenContext
        """
        super().__init__(stack=stack, context=context)
        
    @property
    def context(self) -> TokenContext:
        return self.context
    
    @property
    def stack(self) -> List[Token]:
        return self.stack