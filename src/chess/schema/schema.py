# src/chess/schema/schema.py

"""
Module: chess.schema.schema
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from enum import Enum
from typing import List


from chess.scalar import Scalar
from chess.geometry import Quadrant
from chess.system import GameColor, ROW_SIZE, SearchResult
from chess.formation import BattleOrder, BattleOrderLookup, OrderContext


class Schema(Enum):
    """
    # ROLE: Build Configuration Table, Schema, Metadata Set

    # RESPONSIBILITIES:
    1.  Provides table of metadata used for building Team objects.

    # PARENT:
        *   Enum
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   color (GameColor)
        *   rank_row (int)
        *   pawn_row (int)
        *   advancing_step (Scalar)
        *   home_quadrant (Quadrant)

    # INHERITED ATTRIBUTES:
        * name (str) -->  Name give to each Enum entry.
    """
    def __new__(
            cls,
            color: GameColor,
            rank_row: int,
            advancing_step: Scalar,
            home_quadrant: Quadrant,
    ):
        obj = object.__new__(cls)
        obj._color = color
        obj._rank_row = rank_row
        obj._advancing_step = advancing_step
        obj._home_quadrant = home_quadrant
        return obj
    
    WHITE = (GameColor.WHITE, 0, Scalar(1), Quadrant.N,)
    BLACK = (GameColor.BLACK, (ROW_SIZE - 1), Scalar(-1), Quadrant.S,)
    
    @property
    def color(self) -> GameColor:
        return self._color
    
    @property
    def advancing_step(self) -> Scalar:
        return self._advancing_step
    
    @property
    def home_quadrant(self) -> Quadrant:
        return self.home_quadrant
    
    @property
    def rank_row(self) -> int:
        return self._rank_row
    
    @property
    def pawn_row(self) -> int:
        return self._rank_row + self._advancing_step.value
    
    @property
    def battle_order(self) -> SearchResult[List[BattleOrder]]:
            return BattleOrderLookup().lookup(context=OrderContext(color=self._color))
    
    def __str__(self) -> str:
        return (
            f"color:{self._color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row:{self.pawn_row}]"
        )