# src/chess/team/schema/schema.py

"""
Module: chess.team.schema.schema
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from enum import Enum
from typing import List


from chess.scalar import Scalar
from chess.geometry import Quadrant
from chess.system import GameColor, ROW_SIZE
from chess.formation import BattleOrder, BattleOrderService


class TeamSchema(Enum):
    """
    # ROLE: Schema, Configuration Settings
  
    # RESPONSIBILITIES:
    1.  Unify static metadata about a Team object.
    2.  Name and color details for turn synchronization.
    3.  Details about a Team's deployment and advance on a Board.
    
    # PARENT:
        *   Enum
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   designation (str)
        *   color (GameColor)
        *   rank_row (int)
        *   pawn_row (int)
        *   advancing_step (Scalar)
        *   home_quadrant (Quadrant)
    
    # INHERITED ATTRIBUTES:
    None
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
    def letter(self) -> str:
        return self.name[0]
    
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
    
    # @property
    # def enemy_schema(self) -> TeamSchema:
    #     return TeamSchema.BLACK if self == TeamSchema.WHITE else TeamSchema.WHITE
    
    @property
    def battle_order(self) -> List[BattleOrder]:
        if self.color == GameColor.WHITE:
            return BattleOrderService().white_battle_orders
        return BattleOrderService().black_battle_orders
        
    #
    # @classmethod
    # def find_by_color(cls, color: GameColor) -> TeamSchema:
    #     if color in cls.__members__:
    #         return cls.__members__[color]
    #
    # @classmethod
    # def find_by_name(cls, designation: str) -> TeamSchema:
    #     if designation in cls.__members__:
    #         return cls.__members__[designation]
    
    # @classmethod
    # def allowed_colors(cls) -> List[GameColor]:
    #     return [member.color for member in cls]
    #
    # @classmethod
    # def allowed_names(cls) -> List[str]:
    #     return [member.designation for member in cls]
    
    def __str__(self) -> str:
        return (
            f"color:{self._color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row:{self.pawn_row}]"
        )
