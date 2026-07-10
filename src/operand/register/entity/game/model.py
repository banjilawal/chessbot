# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import GameNullException
from operand import EntityRegister, Game


class GameEntityRegister(EntityRegister[Game]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Game
        null_exception: GameNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Game = Type[Game],
            null_exception: GameNullException = GameNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Game:
        return cast(Game, self.a)
    
    @property
    def null_exception(self) -> GameNullException:
        return cast(GameNullException, self.null_exception)
    
    @property
    def game(self) -> Game:
        return self.operand
    
    @property
    def is_game_entity_register(self) -> bool:
        return isinstance(self, GameEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
