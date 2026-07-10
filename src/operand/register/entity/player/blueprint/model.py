# src/operand/register/entity/player/blueprint/operand.py

"""
Module: operand.register.entity.player.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import PlayerBlueprint
from err import PlayerBlueprintNullException
from operand import EntityRegister


class PlayerBlueprintEntityRegister(EntityRegister[PlayerBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: PlayerBlueprint
        null_exception: PlayerBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: PlayerBlueprint = Type[PlayerBlueprint],
            null_exception: PlayerBlueprintNullException = PlayerBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> PlayerBlueprint:
        return cast(PlayerBlueprint, self.operand)
    
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
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
