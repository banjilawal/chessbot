# src/chess/formation/order.py

"""
Module: chess.formation.order
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from enum import Enum

from chess.persona import Persona
from chess.system import GameColor

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
    *   Team uses its schema attribute to direct Piece objects in its roster the direction of their advance.
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

class Formation(Enum):
    """
    # ROLE: Build Configuration Table, Schema, Metadata Set

    # RESPONSIBILITIES:
    1.  Supply parameters to Piece builders and factories.

    # PARENT:
        *   Enum

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   square_name (str)
        *   color (GameColor)
        *   name (str)
        *   roster_number (int)
        *   persona (Persona)

    # INHERITED ATTRIBUTES:
        * name (str) -->  Name give to each Enum entry.
    """
    def __new__(
            cls,
            square_name: str,
            color: GameColor,
            designation: str,
            roster_number: int,
            persona: Persona,
    ):
        obj = object.__new__(cls)
        obj._square_name = square_name
        obj._color = color
        obj._designation = designation
        obj._roster_number = roster_number
        obj._persona = persona
        return obj
    
    BLACK_KING_CASTLE = ("A1", GameColor.BLACK, "BC1", 1, Persona.ROOK)
    BLACK_KING_KNIGHT = ("B1", GameColor.BLACK, "BN1", 2, Persona.KNIGHT)
    BLACK_KING_BISHOP = ("BB1", GameColor.BLACK, "C1", 3, Persona.BISHOP)
    BLACK_KING = ("D1", GameColor.BLACK, "BK", 4, Persona.KING)
    BLACK_QUEEN = ("E1", GameColor.BLACK, "BQ", 5, Persona.QUEEN)
    BLACK_QUEEN_BISHOP = ("F1", GameColor.BLACK, "BB2", 6, Persona.BISHOP)
    BLACK_QUEEN_KNIGHT = ("G1", GameColor.BLACK, "BN2", 7, Persona.KNIGHT)
    BLACK_QUEEN_CASTLE = ("H1", GameColor.BLACK, "BC2", 8, Persona.ROOK)
    
    BLACK_PAWN_1 = ("A2", GameColor.BLACK, "BP1", 9, Persona.PAWN)
    BLACK_PAWN_2 = ("B2", GameColor.BLACK, "BP2", 10, Persona.PAWN)
    BLACK_PAWN_3 = ("C2", GameColor.BLACK, "BP3", 11, Persona.PAWN)
    BLACK_PAWN_4 = ("D2", GameColor.BLACK, "BP4", 12, Persona.PAWN)
    BLACK_PAWN_5 = ("E2",  GameColor.BLACK, "BP5", 13, Persona.PAWN)
    BLACK_PAWN_6 = ("F2", GameColor.BLACK, "BP6", 14, Persona.PAWN)
    BLACK_PAWN_7 = ("G2", GameColor.BLACK, "BP8", 15, Persona.PAWN)
    BLACK_PAWN_8 = ("H2", GameColor.BLACK, "BP8", 16, Persona.PAWN)
    
    WHITE_KING_CASTLE = ("A8", GameColor.WHITE, "WC1", 1, Persona.ROOK)
    WHITE_KING_KNIGHT = ("B8", GameColor.WHITE, "WN1", 2, Persona.KNIGHT)
    WHITE_KING_BISHOP = ("C8", GameColor.WHITE, "WB1", 3, Persona.BISHOP)
    WHITE_KING = ("D8", GameColor.WHITE, "WK", 4, Persona.KING)
    WHITE_QUEEN = ("E8", GameColor.WHITE, "WQ", 5, Persona.QUEEN)
    WHITE_QUEEN_BISHOP = ("F8", GameColor.WHITE, "WB2", 6, Persona.BISHOP)
    WHITE_QUEEN_KNIGHT = ("G8", GameColor.WHITE, "WN2", 7, Persona.KNIGHT)
    WHITE_QUEEN_CASTLE = ("H8", GameColor.WHITE, "WC2", 8, Persona.ROOK)
    
    WHITE_PAWN_1 = ("A7", GameColor.WHITE, "WP1", 9, Persona.PAWN)
    WHITE_PAWN_2 = ("B7", GameColor.WHITE, "WP2", 10, Persona.PAWN)
    WHITE_PAWN_3 = ("C7", GameColor.WHITE, "WP3", 11, Persona.PAWN)
    WHITE_PAWN_4 = ("D7", GameColor.WHITE, "WP4", 12, Persona.PAWN)
    WHITE_PAWN_5 = ("E7", GameColor.WHITE, "WP5", 13, Persona.PAWN)
    WHITE_PAWN_6 = ("F7", GameColor.WHITE, "WP6", 14, Persona.PAWN)
    WHITE_PAWN_7 = ("G7", GameColor.WHITE, "WP7", 15, Persona.PAWN)
    WHITE_PAWN_8 = ("H7", GameColor.WHITE, "WP8", 16, Persona.PAWN)
    
    @property
    def designation(self) -> str:
        """Common chess name of the Piece."""
        return self._designation
    
    @property
    def color(self) -> GameColor:
        """Matches the Team's color"""
        return self._color
    
    @property
    def square(self) -> str:
        """Name of the Square a piece makes its opening move from."""
        return self._square_name
    
    @property
    def persona(self) -> Persona:
        """Configuration entry for the Piece's rank."""
        return self._persona
    
    @property
    def roster_number(self) -> int:
        """Number assigned to the Piece by its Team"""
        return self._roster_number