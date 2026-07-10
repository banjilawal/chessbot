# src/model/register/entity/square/blueprint/model.py

"""
Module: model.register.entity.square.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import SquareBlueprint
from err import SquareBlueprintNullException
from model import EntityRegister


class SquareBlueprintEntityRegister(EntityRegister[SquareBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: SquareBlueprint
        null_exception: SquareBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: SquareBlueprint = Type[SquareBlueprint],
            null_exception: SquareBlueprintNullException = SquareBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> SquareBlueprint:
        return cast(SquareBlueprint, self.model)
    
    @property
    def null_exception(self) -> SquareBlueprintNullException:
        return cast(SquareBlueprintNullException, self.null_exception)
    
    @property
    def is_square_blueprint_entity_register(self) -> bool:
        return isinstance(self, SquareBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
