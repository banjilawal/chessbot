# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import TokenNullException
from operand import EntityRegister, Token


class TokenEntityRegister(EntityRegister[Token]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Token
        null_exception: TokenNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(self, operand: Token = Type[Token], null_exception: TokenNullException = TokenNullException(),):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Token:
        return cast(Token, self.a)
    
    @property
    def null_exception(self) -> TokenNullException:
        return cast(TokenNullException, self.null_exception)
    
    @property
    def token(self) -> Token:
        return self.operand
    
    @property
    def is_token_entity_register(self) -> bool:
        return isinstance(self, TokenEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
