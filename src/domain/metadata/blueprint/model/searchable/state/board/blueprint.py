# src/domain/metadata/blueprint/model/searchable/state/board/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import SquareDatabase
from domain import Board, BoardSearchContext, BoardTeamColorBinder, StateModelBlueprint
from err import BoardNullException


class BoardBlueprint(StateModelBlueprint[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Board object.

     Attributes:
        id: Optional[int]
        squares: SquareDatabase
        team_binder: BoardTeamColorBinder
        
        domain_class: Type[Board]
        search_context_class: BoardSearchContext
        domain_null_exception: BoardNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _squares: SquareDatabase
    _team_binder: BoardTeamColorBinder
    
    def __init__(
            self,
            squares: SquareDatabase,
            team_binder: BoardTeamColorBinder,
            domain_class: Type[Board],
            search_context_class: Type[BoardSearchContext],
            domain_null_exception: BoardNullException,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[Board]
            search_context_class: BoardSearchContext
            domain_null_exception: BoardNullException
            id: Optional[int]
            squares: SquareDatabase
            team_binder: BoardTeamColorBinder
        """
        super().__init__(
            id=id,
            domain_class=domain_class,
            search_context_class=search_context_class,
            domain_null_exception=domain_null_exception,
        )
        self._squares = squares
        self._team_binder = team_binder
    
    @property
    def domain_class(self) -> Type[Board]:
        return cast(Type[Board], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[BoardSearchContext]:
        return cast(Type[BoardSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> BoardNullException:
        return cast(BoardNullException, super().domain_null_exception)
    
    @property
    def squares(self) -> SquareDatabase:
        return self._squares
    
    @property
    def team_binder(self) -> BoardTeamColorBinder:
        return self._team_binder
    

