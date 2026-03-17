# src/logic/board/analyzer/context.py

"""
Module: logic.board.analyzer.context
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board
from logic.square import Square
from logic.system import Context
from logic.team import Team


class BoardRelationAnalysisContext(Context[Board]):
    _board: Board
    _team: Optional[Team]
    _square: Optional[Square]
    
    def __init__(
            self,
            board: Board,
            team: Optional[Team],
            square: Optional[Square],
    ):
        super().__init__()
        self._board = board
        self._team = team
        self._square = square
        
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def square(self) -> Optional[Square]:
        return self._square
    
    def to_dict(self) -> dict:
        return {
            "board": self._board,
            "team": self._team,
            "square": self._square,
        }
    
