# src/domain/metadata/blueprint/model/searchable/state/team/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import TokenDatabase
from domain import Archetype, Board, Player, StateModelBlueprint, Team, TeamContext
from err import TeamNullException


class TeamBlueprint(StateModelBlueprint[Team]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Team object.

     Attributes:
        board: Board
        owner: Player
        archetype: Archetype
        roster: Optional[TokenDatabase]
        id: Optional[int]
        
        domain_class: Type[Team]
        domain_null_exception: TeamNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _board: Board
    _owner: Player
    _archetype: Archetype
    _roster: Optional[TokenDatabase]
    
    def __init__(
            self,
            board: Board,
            owner: Player,
            archetype: Archetype,
            roster: Optional[TokenDatabase] | None = None,
            domain_class: Optional[Type[Team]] | None = None,
            domain_null_exception: Optional[TeamNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            board: Board
            owner: Player
            archetype: Archetype
            roster: Optional[TokenDatabase]
            domain_class: Optional[Type[Team]]
            domain_null_exception: Optional[TeamNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Team],
            domain_null_exception=domain_null_exception or TeamNullException(),
        )
        self._board = board
        self._owner = owner
        self._archetype = archetype
        self._roster = roster or TokenDatabase()
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype
    
    @property
    def roster(self) -> TokenDatabase:
        return self._roster
    
    @property
    def domain_class(self) -> Type[Team]:
        return cast(Type[Team], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TeamNullException:
        return cast(TeamNullException, super().domain_null_exception)
    
