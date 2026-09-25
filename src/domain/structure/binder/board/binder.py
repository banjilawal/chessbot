# src/domain/structure/binder/board/binder.py

"""
Module: domain.structure.binder.board.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from config import GameColor
from domain import ColorBinder, Board, Team


class BoardTeamColorBinder(ColorBinder[Board, Team]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Maps the Team correctly to its color slot on the Board.
        
    Attributes:
        id: int
        primary: Board
        white_team: Team
        black_team: Team
        
    Provides:
        
    Super Class:
       ColorBinder
    """
    _entry: Dict[GameColor, Team]
    
    def __init__(
            self,
            id: int,
            primary: Board,
            white_team: Team,
            black_team: Team,
            max_capacity: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            primary: Board
            white_team: Team
            black_team: Team
            max_capacity: Optional[int]
        """
        super().__init__(
            id=id,
            primary=primary, 
            max_capacity=max_capacity or self.MAX_CAPACITY,
        )
        self._entry = {
            GameColor.WHITE: white_team,
            GameColor.BLACK: black_team,
        }
        
    @property
    def primary(self) -> Board:
        return cast(Board, super().primary)
    
    @property
    def white_team(self) -> Team:
        return self._entry[GameColor.WHITE]
    
    @property
    def black_team(self) -> Team:
        return self._entry[GameColor.BLACK]
    
    @property
    def to_dict(self) -> Dict[GameColor, Team]:
        return self._entry
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardTeamColorBinder):
            return self.id == other.id
        return False
        
    def __hash__(self):
        return hash(self.id)

        
    