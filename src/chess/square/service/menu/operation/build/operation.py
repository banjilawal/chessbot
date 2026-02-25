# src/chess/square/service/menu/operation/operation.py

"""
Module: chess.square.service.menu.operation.operation
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Dict

from chess.board import Board
from chess.coord import Coord


class SquareBuildOperation:
    """
    A class representing a service operation.
    """
    
    OPERATION_NAME = "build_square"
    PARAMS = Dict[
        "id": int,
        "name" : str,
        "board": Board,
        "coord": Coord,
    ]
    _name: str
    _params: Dict[str: Any]
    
    def __init__(
            self,
            name: str = OPERATION_NAME,
            params: Dict[str, Any] = PARAMS
    ):
        self._name = name
        self._params = params
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def parameters(self) -> Dict[str, Any]:
        return self._params
    
    @classmethod
    def key(cls) -> SquareBuildOperation
        return cls.(name=cls.OPERATION_NAME, params=cls.PARAMS)