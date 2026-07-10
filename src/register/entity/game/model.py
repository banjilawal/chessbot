# src/model/register/entity/model.py

"""
Module: model.register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import GameNullException
from model import EntityRegister, Game


class GameEntityRegister(EntityRegister[Game]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Game
        null_exception: GameNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Game = Type[Game],
            null_exception: GameNullException = GameNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Game:
        return cast(Game, self.a)
    
    @property
    def null_exception(self) -> GameNullException:
        return cast(GameNullException, self.null_exception)
    
    @property
    def game(self) -> Game:
        return self.model
    
    @property
    def is_game_entity_register(self) -> bool:
        return isinstance(self, GameEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
