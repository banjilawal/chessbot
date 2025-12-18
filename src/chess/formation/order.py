# src/chess/formation/order.py

"""
Module: chess.formation.order
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from enum import Enum

from chess.rank import RankSpec
from chess.system import GameColor


class BattleOrder(Enum):
    """
    # ROLE: Build Configuration Table, Schema, Metadata Set

    # RESPONSIBILITIES:
    1.  Provides table of metadata used for building Piece objects.

    # PARENT:
        *   Enum

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   square (str)
        *   color (GameColor)
        *   designation (str)
        *   roster_number (int)
        *   rank_spec (RankSpec)

    # INHERITED ATTRIBUTES:
        * name (str) -->  Name give to each Enum entry.
    """
    def __new__(
            cls,
            square: str,
            color: GameColor,
            designation: str,
            roster_number: int,
            rank_spec: RankSpec,
    ):
        obj = object.__new__(cls)
        obj._square = square
        obj._color = color
        obj._designation = designation
        obj._roster_number = roster_number
        obj._rank_spec = rank_spec
        return obj
    
    BLACK_KING_CASTLE = ("A1", GameColor.BLACK, "BC1", 1, RankSpec.ROOK)
    BLACK_KING_KNIGHT = ("B1", GameColor.BLACK, "BN1", 2, RankSpec.KNIGHT)
    BLACK_KING_BISHOP = ("BB1", GameColor.BLACK, "C1", 3, RankSpec.BISHOP)
    BLACK_KING = ("D1", GameColor.BLACK, "BK", 4, RankSpec.KING)
    BLACK_QUEEN = ("E1", GameColor.BLACK, "BQ", 5, RankSpec.QUEEN)
    BLACK_QUEEN_BISHOP = ("F1", GameColor.BLACK, "BB2", 6, RankSpec.BISHOP)
    BLACK_QUEEN_KNIGHT = ("G1", GameColor.BLACK, "BN2", 7, RankSpec.KNIGHT)
    BLACK_QUEEN_CASTLE = ("H1", GameColor.BLACK, "BC2", 8, RankSpec.ROOK)
    
    BLACK_PAWN_1 = ("A2", GameColor.BLACK, "BP1", 9, RankSpec.PAWN)
    BLACK_PAWN_2 = ("B2", GameColor.BLACK, "BP2", 10, RankSpec.PAWN)
    BLACK_PAWN_3 = ("C2", GameColor.BLACK, "BP3", 11, RankSpec.PAWN)
    BLACK_PAWN_4 = ("D2", GameColor.BLACK, "BP4", 12, RankSpec.PAWN)
    BLACK_PAWN_5 = ("E2",  GameColor.BLACK, "BP5", 13, RankSpec.PAWN)
    BLACK_PAWN_6 = ("F2", GameColor.BLACK, "BP6", 14, RankSpec.PAWN)
    BLACK_PAWN_7 = ("G2", GameColor.BLACK, "BP8", 15, RankSpec.PAWN)
    BLACK_PAWN_8 = ("H2", GameColor.BLACK, "BP8", 16, RankSpec.PAWN)
    
    WHITE_KING_CASTLE = ("A8", GameColor.WHITE, "WC1", 1, RankSpec.ROOK)
    WHITE_KING_KNIGHT = ("B8", GameColor.WHITE, "WN1", 2, RankSpec.KNIGHT)
    WHITE_KING_BISHOP = ("C8", GameColor.WHITE, "WB1", 3, RankSpec.BISHOP)
    WHITE_KING = ("D8", GameColor.WHITE, "WK", 4, RankSpec.KING)
    WHITE_QUEEN = ("E8", GameColor.WHITE, "WQ", 5, RankSpec.QUEEN)
    WHITE_QUEEN_BISHOP = ("F8", GameColor.WHITE, "WB2", 6, RankSpec.BISHOP)
    WHITE_QUEEN_KNIGHT = ("G8", GameColor.WHITE, "WN2", 7, RankSpec.KNIGHT)
    WHITE_QUEEN_CASTLE = ("H8", GameColor.WHITE, "WC2", 8, RankSpec.ROOK)
    
    WHITE_PAWN_1 = ("A7", GameColor.WHITE, "WP1", 9, RankSpec.PAWN)
    WHITE_PAWN_2 = ("B7", GameColor.WHITE, "WP2", 10, RankSpec.PAWN)
    WHITE_PAWN_3 = ("C7", GameColor.WHITE, "WP3", 11, RankSpec.PAWN)
    WHITE_PAWN_4 = ("D7", GameColor.WHITE, "WP4", 12, RankSpec.PAWN)
    WHITE_PAWN_5 = ("E7", GameColor.WHITE, "WP5", 13, RankSpec.PAWN)
    WHITE_PAWN_6 = ("F7", GameColor.WHITE, "WP6", 14, RankSpec.PAWN)
    WHITE_PAWN_7 = ("G7", GameColor.WHITE, "WP7", 15, RankSpec.PAWN)
    WHITE_PAWN_8 = ("H7", GameColor.WHITE, "WP8", 16, RankSpec.PAWN)
    
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
        return self._square
    
    @property
    def rank_spec(self) -> RankSpec:
        """Configuration entry for the Piece's rank."""
        return self._rank_spec
    
    @property
    def roster_number(self) -> int:
        """Number assigned to the Piece by its Team"""
        return self._roster_number