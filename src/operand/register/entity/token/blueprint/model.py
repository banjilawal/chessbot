# src/operand/register/entity/token/blueprint/operand.py

"""
Module: operand.register.entity.token.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import TokenBlueprint
from err import TokenBlueprintNullException
from operand import EntityRegister


class TokenBlueprintEntityRegister(EntityRegister[TokenBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: TokenBlueprint
        null_exception: TokenBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: TokenBlueprint = Type[TokenBlueprint],
            null_exception: TokenBlueprintNullException = TokenBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> TokenBlueprint:
        return cast(TokenBlueprint, self.operand)
    
    @property
    def null_exception(self) -> TokenBlueprintNullException:
        return cast(TokenBlueprintNullException, self.null_exception)
    
    @property
    def is_token_blueprint_entity_register(self) -> bool:
        return isinstance(self, TokenBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
