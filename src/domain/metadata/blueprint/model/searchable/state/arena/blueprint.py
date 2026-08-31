# src/domain/metadata/blueprint/model/searchable/state/arena/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Arena, ArenaPlayerColorBinder, ArenaContext, Board, Game, StateModelBlueprint
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
        search_context_class: Type[ArenaContext]
        domain_null_exception: ArenaNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _game: Game
    _board: Board
    _player_binder: ArenaPlayerColorBinder
    
    def __init__(
            self,
            game: Game,
            board: Board,
            player_binder: ArenaPlayerColorBinder,
            domain_class: Optional[Type[Arena]] | None = None,
            domain_null_exception: Optional[ArenaNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            game: Game
            board: Board
            player_binder: ArenaPlayerColorBinder
            domain_class: Optional[Type[Arena]]
            domain_null_exception: Optional[ArenaNullException]
            id: Optional[int]

        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Arena],
            domain_null_exception=domain_null_exception or ArenaNullException(),
        )
        self._game = game
        self._board = board
        self._player_binder = player_binder
    
    @property
    def game(self) -> Game:
        return self._game
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def player_binder(self) -> ArenaPlayerColorBinder:
        return self._player_binder
    
    @property
    def domain_class(self) -> Type[Arena]:
        return cast(Type[Arena], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArenaNullException:
        return cast(ArenaNullException, super().domain_null_exception)
    

