# src/chess/schema/schema.py

"""
Module: chess.schema.schema
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from enum import Enum

from chess.schema import Schema
from chess.scalar import Scalar
from chess.geometry import Quadrant
from chess.system import GameColor, NUMBER_OF_ROWS


class Schema(Enum):
    """
    # ROLE: Build Configuration Table, Schema, Metadata Set
    
    # ABOUT THE SCHEMA:
    The Schema implements a hashtable which a Team gets metadata about its initial deployment on the Board
    and how it advances. The color assigned to the Team is the Schema table's key.

    ## STRUCTURE OF THE SCHEMA HASHTABLE:
        *   Key (str)
        *   Value   (List{str: Any})
        
    ### Schema Vale: List[{str: Any}] each tuple in the list represents {Schema.Entry.attribute: attribute_value}

    ## WHO USES THE SCHEMA TABLE:
        *   TeamBuilder uses a Schema.ELEMENT/ENTRY to create a Team object.
        *   Team uses its schema attribute to direct Token objects in its roster the direction of their advance.
        *   TeamFinder can use the hashtable key to find Teams which match either the GameColor
        *   Other EntityFinder classes can use the Team.schema attribute to filter by their entity.team.schema attribute.

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
    BLACK = (GameColor.BLACK, (NUMBER_OF_ROWS - 1), Scalar(-1), Quadrant.S,)
    
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
    def opposite(self) -> Schema:
        if self == Schema.WHITE:
            return Schema.BLACK
        return Schema.WHITE
    #
    # @property
    # def battle_order(self) -> SearchResult[List[Formation]]:
    #         return BattleOrderLookup().lookup(map=OrderContext(color=self._color))
    
    def __str__(self) -> str:
        return (
            f"color:{self._color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row:{self.pawn_row}]"
        )