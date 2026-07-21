# src/blueprint/model/state/team/blueprint.py

"""
Module: blueprint.model.state.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import StateModelBlueprint
from consistency.arena.checker import ArenaConsistencyChecker
from model import Board, Player, Team
from schema import Archetype


class TeamBlueprint(StateModelBlueprint[Team]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Team object.

    Attributes:
        board: Board,
        owner: Player
        archetype: Archetype
        model_class: Type[Team]
        
    Provides:

     Super Class:
        StateModelBlueprint
     """
    _board: Board
    _owner: Player
    _archetype: Archetype
    
    def __init__(
            self,
            board: Board,
            owner: Player,
            archetype: Archetype,
            id: Optional[int] | None = None,
            model_class: Type[Team] = Team,
    ):
        """
        Args:
            board: Board
            owner: Player
            archetype: Archetype,
            model_class: Type[Team] = Type[Team]            
        """
        super().__init__(id=id, model_class=model_class)
        self._board = board
        self._owner = owner
        self._archetype = archetype
        
    @property
    def model_class(self) -> Type[Team]:
        return cast(Type[Team], super().model_class)
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype