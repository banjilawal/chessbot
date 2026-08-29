# src/domain/metadata/blueprint/model/searchable/state/arena/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Arena, ArenaPlayerColorBinder, ArenaSearchContext, Board, StateModelBlueprint
from err import ArenaNullException


class ArenaBlueprint(StateModelBlueprint[Arena]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating an Arena object.

     Attributes:
        id: Optional[int]
        board: Board
        player_binder: ArenaPlayerColorBinder
        
        domain_class: Type[Arena]
        search_context_class: Type[ArenaSearchContext]
        domain_null_exception: ArenaNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _board: Board
    _player_binder: ArenaPlayerColorBinder
    
    def __init__(
            self,
            board: Board,
            player_binder: ArenaPlayerColorBinder,
            domain_class: Optional[Type[Arena]] | None = None,
            search_context_class: Optional[Type[ArenaSearchContext]] | None = None,
            domain_null_exception: Optional[ArenaNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Arena]] | None = None,
            search_context_class: Optional[Type[ArenaSearchContext]] | None = None,
            domain_null_exception: Optional[ArenaNullException] | None = None,
            id: Optional[int]
            board: Board
            player_binder: ArenaPlayerColorBinder
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Arena],
            search_context_class=search_context_class or Type[ArenaSearchContext],
            domain_null_exception=domain_null_exception or ArenaNullException(),
        )
        self._board = board
        self._player_binder = player_binder
    
    @property
    def domain_class(self) -> Type[Arena]:
        return cast(Type[Arena], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[ArenaSearchContext]:
        return cast(Type[ArenaSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> ArenaNullException:
        return cast(ArenaNullException, super().domain_null_exception)
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def player_binder(self) -> ArenaPlayerColorBinder:
        return self._player_binder
