# src/domain/metadata/blueprint/search/arena/blueprint.py

"""
Module: domain.metadata.blueprint.search.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from config import GameColor
from domain import ArenaSearchContext, Board, Game, SearchContextBlueprint, Team
from err import ArenaSearchContextNullException


class ArenaContextBlueprint(SearchContextBlueprint[ArenaSearchContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an ArenaSearchContext.
         
     Attributes:
        domain_class: Type[ArenaSearchContext]
        domain_null_exception: ArenaSearchContextNullException

     Provides:

     Super Class:
        SearchContextBlueprint
     """

    _game: Optional[Game]
    _team: Optional[Team]
    _board: Optional[Board]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            domain_class: Optional[Type[ArenaSearchContext]] | None = None,
            domain_null_exception: Optional[ArenaSearchContextNullException] | None = None,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            team: Optional[Team] | None = None,
            board: Optional[Board] | None = None,
            color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            domain_class: Type[ArenaSearchContext]
            domain_null_exception: ArenaSearchContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[ArenaSearchContext],
            domain_null_exception=domain_null_exception or ArenaSearchContextNullException(),
        )
        self._game = game
        self._team = team
        self._board = board
        self._color = color
    
    @property
    def domain_class(self) -> Type[ArenaSearchContext]:
        return cast(Type[ArenaSearchContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArenaSearchContextNullException:
        return  cast(ArenaSearchContextNullException, super()._domain_null_exception)
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color


