# src/model/register/entity/token/blueprint/model.py

"""
Module: model.register.entity.token.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import TokenBlueprint
from err import TokenBlueprintNullException
from model import EntityRegister


class TokenBlueprintEntityRegister(EntityRegister[TokenBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: TokenBlueprint
        null_exception: TokenBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: TokenBlueprint = Type[TokenBlueprint],
            null_exception: TokenBlueprintNullException = TokenBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> TokenBlueprint:
        return cast(TokenBlueprint, self.model)
    
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
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
