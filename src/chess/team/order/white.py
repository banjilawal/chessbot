# src/chess/team/order/white.py

"""
Module: chess.team.order.white
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from enum import Enum
from typing import List, Optional

from chess.rank import RankSpec
from chess.square import Square


class WhiteBattleOrder(Enum):
    def __new__(
            cls,
            piece_name: str,
            square_name: str,
            roster_number: int,
            rank_spec: RankSpec,
    ):
        obj = object.__new__(cls)
        obj._piece_name = piece_name
        obj._square_name = square_name
        obj._roster_number = roster_number
        obj._rank_spec = rank_spec
        return obj
    
    WHITE_KING_CASTLE = ("WC1", "A8", 1, RankSpec.ROOK)
    WHITE_KING_KNIGHT = ("WN1", "B8", 2, RankSpec.KNIGHT)
    WHITE_KING_BISHOP = ("WB1", "C8", 3, RankSpec.BISHOP)
    WHITE_KING = ("WK", "D8", 4, RankSpec.KING)
    WHITE_QUEEN = ("WQ", "E8", 5, RankSpec.QUEEN)
    WHITE_QUEEN_BISHOP = ("WB2", 6, "F8", RankSpec.BISHOP)
    WHITE_QUEEN_KNIGHT = ("WN2", 7, "G8", RankSpec.KNIGHT)
    WHITE_QUEEN_CASTLE = ("WC2", 8, "H8", RankSpec.ROOK)
    
    WHITE_PAWN_1 = ("WP1", "A7", 9, RankSpec.PAWN)
    WHITE_PAWN_2 = ("WP2", "B7", 10, RankSpec.PAWN)
    WHITE_PAWN_3 = ("WP3", "C7", 11, RankSpec.PAWN)
    WHITE_PAWN_4 = ("WP4", "D7", 12, RankSpec.PAWN)
    WHITE_PAWN_5 = ("WP5", "E7", 13, RankSpec.PAWN)
    WHITE_PAWN_6 = ("WP6", "F7", 14, RankSpec.PAWN)
    WHITE_PAWN_7 = ("WP7", "G7", 15, RankSpec.PAWN)
    WHITE_PAWN_8 = ("WP8", "H7", 16, RankSpec.PAWN)

    @property
    def piece_name(self) -> str:
        return self._piece_name
    
    @property
    def square_name(self) -> str:
        return self._square_name
    
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
    def upper_case_piece_names(cls) -> List[str]:
        return [member.piece_name.upper() for member in cls]
    
    @classmethod
    def upper_case_square_names(cls) -> List[str]:
        return [member.square_name.upper() for member in cls]
    
    @classmethod
    def find_order_by_square(cls, square: Square) -> Optional[WhiteBattleOrder]:
        for member in cls:
            if member.square_name.upper() == square.name.upper():
                return member
        return None
    
    @classmethod
    def find_order_by_piece(cls, piece: Piece) -> Optional[WhiteBattleOrder]:
        """
        Finding by piece_name avoids getting a hit when searching for an opposite
        piece by mistake.
        """
        for member in cls:
            if member.piece_name.upper() == piece.name.upper():
                return member
        return None