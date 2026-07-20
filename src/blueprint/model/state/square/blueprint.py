# src/blueprint/model/state/square/blueprint.py

"""
Module: blueprint.model.state.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import StateModelBlueprint
from model import Board, Coord, Square
from schema import Formation


class SquareBlueprint(StateModelBlueprint[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Square object.

    Attributes:
        board: Board,
        coord: Coord
        formation Optional[Formation]
        model_class: Type[Square]
        
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
            model_class: Type[Square] = Square,
    ):
        """
        Args:
            name: str
            board: Board
            coord: Coord
            formation: OptionalFormation
            model_class: Type[Square] = Type[Square]            
        """
        super().__init__(id=id, model_class=model_class)
        self._name = name
        self._board = board
        self._coord = coord
        self._formation = formation
    
    @property
    def model_class(self) -> Type[Square]:
        return cast(Type[Square], self.model_class)
    
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