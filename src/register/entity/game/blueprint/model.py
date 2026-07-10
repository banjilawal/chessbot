# src/model/register/entity/game/blueprint/model.py

"""
Module: model.register.entity.game.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import GameBlueprint
from err import GameBlueprintNullException
from model import EntityRegister


class GameBlueprintEntityRegister(EntityRegister[GameBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: GameBlueprint
        null_exception: GameBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: GameBlueprint = Type[GameBlueprint],
            null_exception: GameBlueprintNullException = GameBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> GameBlueprint:
        return cast(GameBlueprint, self.model)
    
    @property
    def null_exception(self) -> GameBlueprintNullException:
        return cast(GameBlueprintNullException, self.null_exception)
    
    @property
    def is_game_blueprint_entity_register(self) -> bool:
        return isinstance(self, GameBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
