# src/register/entity/player/blueprint/py

"""
Module: register.entity.player.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import PlayerBlueprint
from err import PlayerBlueprintNullException
from model import EntityRegister


class PlayerBlueprintEntityRegister(EntityRegister[PlayerBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: PlayerBlueprint
        null_exception: PlayerBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: PlayerBlueprint = Type[PlayerBlueprint],
            null_exception: PlayerBlueprintNullException = PlayerBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> PlayerBlueprint:
        return cast(PlayerBlueprint, self.model)
    
    @property
    def null_exception(self) -> PlayerBlueprintNullException:
        return cast(PlayerBlueprintNullException, self.null_exception)
    
    @property
    def is_player_blueprint_entity_register(self) -> bool:
        return isinstance(self, PlayerBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
