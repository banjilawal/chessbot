# src/operand/register/entity/game/blueprint/operand.py

"""
Module: operand.register.entity.game.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import GameBlueprint
from err import GameBlueprintNullException
from operand import EntityRegister


class GameBlueprintEntityRegister(EntityRegister[GameBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: GameBlueprint
        null_exception: GameBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: GameBlueprint = Type[GameBlueprint],
            null_exception: GameBlueprintNullException = GameBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> GameBlueprint:
        return cast(GameBlueprint, self.operand)
    
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
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
