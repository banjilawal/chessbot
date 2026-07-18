# src/blueprint/container/state/square/blueprint.py

"""
Module: blueprint.container.state.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import StateContainerBlueprint
from container import Board, Coord, Square
from schema import Formation


class SquareBlueprint(StateContainerBlueprint[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Square object.

    Attributes:
        board: Board,
        coord: Coord
        formation Optional[Formation]
        container_class: Type[Square]
        
    Provides:

     Super Class:
        StateContainerBlueprint
     """
    _board: Board
    _coord: Coord
    _formation: Optional[Formation]
    
    def __init__(
            self,
            board: Board,
            coord: Coord,
            id: Optional[int] | None = None,
            formation: Optional[Formation] | None = None,
            container_class: Type[Square] = Square,
    ):
        """
        Args:
            board: Board
            coord: Coord
            formation: OptionalFormation
            container_class: Type[Square] = Type[Square]            
        """
        super().__init__(id=id, container_class=container_class)
        self._board = board
        self._coord = coord
        self._formation = formation
    
    @property
    def mode_class(self) -> Type[Square]:
        return cast(Type[Square], self.container_class)
    
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