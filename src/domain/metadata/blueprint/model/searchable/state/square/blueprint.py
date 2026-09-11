# src/domain/metadata/blueprint/model/searchable/state/square/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Board, Coord, Square, SquareState, StateModelBlueprint, Token
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
        occupant: Optional[Token]

        domain_class: Type[Square]
        domain_null_exception: SquareNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _name: str
    _board: Board
    _coord: Coord
    _state: SquareState
    _occupant: Optional[Token]
    
    def __init__(
            self,
            name: str,
            board: Board,
            coord: Coord,
            occupant: Optional[Token] | None = None,
            state: Optional[SquareState] | None = None,
            domain_class: Optional[Type[Square]] | None = None,
            domain_null_exception: Optional[SquareNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            name: str
            board: Board
            coord: Coord
            occupant: Optional[Token]
            state: Optional[SquareState]
            domain_class: Optional[Type[Square]]
            domain_null_exception: Optional[SquareNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Square],
            domain_null_exception=domain_null_exception or SquareNullException(),
        )
        self._name = name
        self._board = board
        self._coord = coord
        self._occupant = occupant
        self._state = state or SquareState.EMPTY
    
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
    def state(self) -> SquareState:
        return self._state
    
    @property
    def occupant(self) -> Optional[Token]:
        return self._occupant
    
    @property
    def domain_class(self) -> Type[Square]:
        return cast(Type[Square], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SquareNullException:
        return cast(SquareNullException, super().domain_null_exception)