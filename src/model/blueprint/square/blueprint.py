# src/model/blueprint/square/blueprint.py

"""
Module: model.blueprint.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Blueprint, Board, Coord, Formation, Square


class SquareBlueprint(Blueprint[Square]):
    _name: str
    _board: Board
    _coord: Coord
    _id: Optional[int]
    _formation: Optional[Formation]
    
    def __init__(
            self,
            name: str,
            board: Board,
            coord: Coord,
            id: Optional[int] | None = None,
            formation: Optional[Formation] | None = None,
    ):
        super().__init__()
        self._id = id
        self._name = name
        self._board = board
        self._coord = coord
        formation = formation
        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def formation(self) -> Optional[Formation]:
        return self._formation
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    

