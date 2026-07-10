# src/model/register/entity/arena/blueprint/model.py

"""
Module: model.register.entity.arena.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ArenaBlueprint
from err import ArenaBlueprintNullException
from model import EntityRegister


class ArenaBlueprintEntityRegister(EntityRegister[ArenaBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: ArenaBlueprint
        null_exception: ArenaBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: ArenaBlueprint = Type[ArenaBlueprint],
            null_exception: ArenaBlueprintNullException = ArenaBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> ArenaBlueprint:
        return cast(ArenaBlueprint, self.model)
    
    @property
    def null_exception(self) -> ArenaBlueprintNullException:
        return cast(ArenaBlueprintNullException, self.null_exception)
    
    @property
    def is_arena_blueprint_entity_register(self) -> bool:
        return isinstance(self, ArenaBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
