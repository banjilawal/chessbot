# src/chess/square/square.py

"""
Module: chess.square.square
Author: Banji Lawal
Created: 2025-07-26
Updated: 2025-10-10

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the ChessBot integrity requirement.
  2. A satisfaction of the ChessBot reliability requirement.

# SECTION 2 - Scope:
The module covers Square objects.

# SECTION 3 - Limitations:
  1. The module has no logic for assuring a Square will not introduce errors.
  2. This module should not be used directly. For constructing a Square use SquareBuilder. Before using a
     Square it must be verified by SquareValidator.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5- Features Supporting Requirements:
No features provided.

# 6 Feature Delivery Mechanism:
No feature delivery mechanisms.

# SECTION 7 - Dependencies:
* From chess.system:
    AutoId, LoggingLevelRouter

* From Python typing Library:
   Optional

# SECTION 8- Contains:
1. Square
"""

from typing import Optional, cast

from chess.coord import Coord
from chess.piece import Piece
from chess.system import LoggingLevelRouter


class Square:
    """
    # ROLE: Data-Holding
  
    # RESPONSIBILITIES:
    1. Places on the Board that a Piece occupies.
  
    # PROVIDES:
    Square
  
    # ATTRIBUTES:
      * _id (int): unique number.
      * _name (str): Unique letter-number combination identifying a Square.
      * _coord (Coord): Row and Column indices where Square is located on a Board instance..
      * _occupant (Optional[Piece]): Piece object that might be occupying the Square.
    """
    _id: int
    _name: str
    _coord: Coord
    _occupant: Optional[Piece]
    
    @LoggingLevelRouter.monitor
    def __init__(self, id: int, name: str, coord: Coord):
        self._id = id
        self._name = name
        self._coord = coord
        self._occupant = None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    @LoggingLevelRouter.monitor
    def coord(self) -> Coord:
        return self._coord
    
    @property
    @LoggingLevelRouter.monitor
    def occupant(self) -> Optional[Piece]:
        return self._occupant
    
    @occupant.setter
    @LoggingLevelRouter.monitor
    def occupant(self, piece: Optional[Piece]):
        self._occupant = piece
    
    def __eq__(self, other: object) -> bool:
        if other is self:
            return True
        if isinstance(other, Square):
            square = cast(Square, other)
            return self._id == square.id
        return False
    
    def __hash__(self) -> int:
        """Returns the hash value of the Square based on its ID."""
        return hash(self._id)
    
    def __str__(self) -> str:
        """Returns team_name string representation of the Square."""
        occupant_str = f" occupant:{self._occupant.name}" if self._occupant else ""
        return f"Square:[{self._id} {self._name} {self._coord}{occupant_str}]"
