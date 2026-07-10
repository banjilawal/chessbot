# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import PlayerNullException
from model import EntityRegister, Player


class PlayerEntityRegister(EntityRegister[Player]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Player
        null_exception: PlayerNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Player = Type[Player],
            null_exception: PlayerNullException = PlayerNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Player:
        return cast(Player, self.a)
    
    @property
    def null_exception(self) -> PlayerNullException:
        return cast(PlayerNullException, self.null_exception)
    
    @property
    def player(self) -> Player:
        return self.model
    
    @property
    def is_player_entity_register(self) -> bool:
        return isinstance(self, PlayerEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
