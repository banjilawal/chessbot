# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import TokenNullException
from model import EntityRegister, Token


class TokenEntityRegister(EntityRegister[Token]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Token
        null_exception: TokenNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(self, model: Token = Type[Token], null_exception: TokenNullException = TokenNullException(),):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Token:
        return cast(Token, self.a)
    
    @property
    def null_exception(self) -> TokenNullException:
        return cast(TokenNullException, self.null_exception)
    
    @property
    def token(self) -> Token:
        return self.model
    
    @property
    def is_token_entity_register(self) -> bool:
        return isinstance(self, TokenEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
