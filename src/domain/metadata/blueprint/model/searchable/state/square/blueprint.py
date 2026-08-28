# src/domain/metadata/blueprint/model/searchable/state/square/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import StateModelBlueprint
from domain.model import Board, Coord, Square
from domain.schema import Formation


class SquareBlueprint(StateModelBlueprint[Square]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Square object.

    Attributes:
        board: Board,
        coord: Coord
        formation Optional[Formation]
        domain_class: Type[Square]
        
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
            id: Optional[int] | None = None,
            formation: Optional[Formation] | None = None,
            domain_class: Type[Square] = Square,
    ):
        """
        Args:
            name: str
            board: Board
            coord: Coord
            formation: OptionalFormation
            domain_class: Type[Square] = Type[Square]
        """
        super().__init__(id=id, domain_class=domain_class)
        self._name = name
        self._board = board
        self._coord = coord
        self._formation = formation
    
    @property
    def domain_class(self) -> Type[Square]:
        return cast(Type[Square], super().domain_class)
    
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