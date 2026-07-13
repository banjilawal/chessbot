# src/schema/archetype/schema.py

"""
Module: schema.archetype.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from enum import Enum

import setting.board.dimension
from model import OldQuadrant, Scalar
from setting import GameColor


class Archetype(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set
        
    Responsibilities:
        1.  Provides table of metadata used for building Team objects.
        
    Attributes:
        rank_row: int
        color: GameColor
        advancing_step: Scalar
        home_quadrant: Quadrant
        
    Provides:
    
    Super Class:
        Enum
    
    About:
        The Archetype implements a hashtable which a Team gets metadata about its initial deployment on
        the Board and how it advances. The color assigned to the Team is the Archetype table's key.

    ## STRUCTURE OF THE ARCHETYPE HASHTABLE:
        *   Key (str)
        *   Value   (List{str: Any})
        
    ### Archetype Vale: List[{str: Any}] each tuple in the list represents {Archetype.Entry.attribute: attribute_value}

    ## WHO USES THE ARCHETYPE TABLE:
        *   TeamBuild uses a Archetype.ELEMENT/ENTRY to create a Team object.
        *   Team uses its archetype attribute to direct Token objects in its roster the direction of their advance.
        *   TeamFinder can use the hashtable key to find Teams which match either the GameColor
        *   Other EntityFinder classes can use the Team.archetype attribute to filter by their entity.team.archetype attribute.

    # INHERITED ATTRIBUTES:
        * archetype (str) -->  Name give to each Enum entry.
    """
    def __new__(
            cls,
            color: GameColor,
            rank_row: int,
            advancing_step: Scalar,
            home_quadrant: OldQuadrant,
    ):
        """
        Args:
            rank_row: int
            color: GameColor
            advancing_step: Scalar
            home_quadrant: Quadrant
        """
        obj = object.__new__(cls)
        obj._color = color
        obj._rank_row = rank_row
        obj._advancing_step = advancing_step
        obj._home_quadrant = home_quadrant
        return obj
    
    WHITE = (GameColor.WHITE, 0, Scalar(1), OldQuadrant.N,)
    BLACK = (GameColor.BLACK, (setting.board.dimension.config.number_of_rows - 1), Scalar(-1), OldQuadrant.S,)
    
    @property
    def color(self) -> GameColor:
        return self._color
    
    @property
    def advancing_step(self) -> Scalar:
        return self._advancing_step
    
    @property
    def home_quadrant(self) -> OldQuadrant:
        return self.home_quadrant
    
    @property
    def rank_row(self) -> int:
        return self._rank_row
    
    @property
    def pawn_row(self) -> int:
        return self._rank_row + self._advancing_step.magnitude
    
    @property
    def enemy_archetype(self) -> Archetype:
        if self == Archetype.WHITE:
            return Archetype.BLACK
        return Archetype.WHITE
    
    def __str__(self) -> str:
        return (
            f"color:{self._color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row:{self.pawn_row}]"
        )