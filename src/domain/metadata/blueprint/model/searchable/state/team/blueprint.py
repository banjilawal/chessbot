# src/domain/metadata/blueprint/model/searchable/state/team/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Archetype, Board, Player, StateModelBlueprint, Team, TeamContext
from err import TeamNullException


class TeamBlueprint(StateModelBlueprint[Team]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Team object.

     Attributes:
        id: Optional[int]
        board: Board
        owner: Player
        archetype: Archetype

        domain_class: Type[Team]
        search_context_class: Type[TeamContext]
        domain_null_exception: TeamNullException

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
            domain_class: Optional[Type[Team]] | None = None,
            search_context_class: Optional[Type[TeamContext]] | None = None,
            domain_null_exception: Optional[TeamNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Team]]
            search_context_class: Optional[Type[TeamContext]]
            domain_null_exception: Optional[TeamNullException]
            id: Optional[int]
            board: Board
            owner: Player
            archetype: Archetype
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Team],
            search_context_class=search_context_class or Type[TeamContext],
            domain_null_exception=domain_null_exception or TeamNullException(),
        )
        self._board = board
        self._owner = owner
        self._archetype = archetype
    
    @property
    def domain_class(self) -> Type[Team]:
        return cast(Type[Team], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[TeamContext]:
        return cast(Type[TeamContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> TeamNullException:
        return cast(TeamNullException, super().domain_null_exception)
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype