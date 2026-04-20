# src/model/blueprint/arena/model.py

"""
Module: model.blueprint.arena.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Game, Blueprint, Arena


class ArenaBlueprint(Blueprint[Arena]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a Arena object.
    
    Attributes:
        id: int
        game: Game
    
    Provides:
    
    Super Class:
        Blueprint
    """
    _id: int
    _game: Game

    
    def __init__(
            self,
            game: Game,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            game: Game
        """
        super().__init__()
        self._id = id
        self._game = game
        
    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def game(self) -> Game:
        return self._game
    

