# src/chess/team/order/black.py

"""
Module: chess.team.order.black
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from enum import Enum
from typing import List, Optional

from chess.piece import Piece
from chess.rank import RankSpec
from chess.square import Square
from chess.system import GameColor


class BattleOrder(Enum):
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
        return self._designation
    
    @property
    def color(self) -> GameColor:
        return self._color
    
    @property
    def square(self) -> str:
        return self._square
    
    @property
    def rank_spec(self) -> RankSpec:
        return self._rank_spec
    
    @property
    def roster_number(self) -> int:
        return self._roster_number
    
    @classmethod
    def allowed_roster_numbers(cls) -> List[int]:
        return [member.roster_number for member in cls]
    
    @classmethod
    def allowed_designations(cls) -> List[str]:
        return [member.designation.upper() for member in cls]
    
    @classmethod
    def allowed_squares(cls) -> List[str]:
        return [member.square.upper() for member in cls]
    
    @classmethod
    def find_order_by_square(cls, square: Square) -> Optional[BlackBattleOrder]:
        for member in cls:
            if member.square.upper() == square.upper():
                return member
        return None
    
    @classmethod
    def find_order_by_piece(cls, piece: Piece) -> Optional[BlackBattleOrder]:
        """
        Finding by piece_designation avoids getting a hit when searching for an opposite
        piece by mistake.
        """
        for member in cls:
            if member.designation.upper() == piece.name.upper():
                return member
        return None