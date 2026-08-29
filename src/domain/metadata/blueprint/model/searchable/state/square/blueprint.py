# src/domain/metadata/blueprint/model/searchable/state/square/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Board, Coord, Formation, Square, SquareSearchContext, StateModelBlueprint
from err import SquareNullException


class SquareBlueprint(StateModelBlueprint[Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Square object.

     Attributes:
        id: Optional[int]
        name: str
        board: Board
        coord: Coord
        formation: Optional[Formation]

        domain_class: Type[Square]
        search_context_class: Type[SquareSearchContext]
        domain_null_exception: SquareNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _name: str
    _board: Board
    _coord: Coord
    _formation: Optional[Formation]
    
    def __init__(
            self,
            name: str,
            board: Board,
            coord: Coord,
            domain_class: Optional[Type[Square]] | None = None,
            search_context_class: Optional[Type[SquareSearchContext]] | None = None,
            domain_null_exception: Optional[SquareNullException] | None = None,
            formation: Optional[Formation] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Square]]
            search_context_class: Optional[Type[SquareSearchContext]]
            domain_null_exception: Optional[SquareNullException]
            id: Optional[int]
            name: str
            board: Board
            coord: Coord
            formation: Optional[Formation]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Square],
            search_context_class=search_context_class or Type[SquareSearchContext],
            domain_null_exception=domain_null_exception or SquareNullException(),
        )
        self._name = name
        self._board = board
        self._coord = coord
        self._formation = formation
    
    @property
    def domain_class(self) -> Type[Square]:
        return cast(Type[Square], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[SquareSearchContext]:
        return cast(Type[SquareSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> SquareNullException:
        return cast(SquareNullException, super().domain_null_exception)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def formation(self) -> Optional[Formation]:
        return self._formation
    
    @property
    def is_home_square_blueprint(self) -> bool:
        return self._formation is not None