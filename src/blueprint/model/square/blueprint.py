# src/blueprint/model/square/blueprint.py

"""
Module: blueprint.model.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import ModelBlueprint
from err import SquareNullException
from model import Board, Coord, Square
from schema import Coord, Formation


class SquareBlueprint(ModelBlueprint[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Square object.

    Attributes:
        board: Board,
        coord: Coord
        id: Optional[int]
        formation Optional[Formation]
        model_class: Type[Square]
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    def __init__(
            self,
            board: Board,
            coord: Coord,
            id: Optional[int] | None = None,
            formation: Optional[Formation] | None = None,
            model_class: Type[Square] = Square,
    ):
        """
        Args:
            board: Board
            coord: Coord
            formation: OptionalFormation
            model_class: Type[Square] = Type[Square]            
        """
        super().__init__(id=id, model_class=model_class)
        self._board = board
        self._coord = coord
        self._formation = formation
        
    @property
    def mode_class(self) -> Type[Square]:
        return cast(Type[Square], self.model_class)
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def is_home_square_blueprint(self) -> bool:
        return self._formation is not None