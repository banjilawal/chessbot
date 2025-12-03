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
from chess.team import BlackBattleOrder


class BlackBattleOrder(Enum):
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
    
    BLACK_KING_CASTLE = ("BC1", "A1", 1, RankSpec.ROOK)
    BLACK_KING_KNIGHT = ("BN1", "B1", 2, RankSpec.KNIGHT)
    BLACK_KING_BISHOP = ("BB1", "C1", 3, RankSpec.BISHOP)
    BLACK_KING = ("BK", "D1", 4, RankSpec.KING)
    BLACK_QUEEN = ("BQ", "E1", 5, RankSpec.QUEEN)
    BLACK_QUEEN_BISHOP = ("BB2", "F1", 6, RankSpec.BISHOP)
    BLACK_QUEEN_KNIGHT = ("BN2", "G1", 7, RankSpec.KNIGHT)
    BLACK_QUEEN_CASTLE = ("BC2", "H1", 8, RankSpec.ROOK)
    
    BLACK_PAWN_1 = ("BP1", "A2", 9, RankSpec.PAWN)
    BLACK_PAWN_2 = ("BP2", "B2", 10, RankSpec.PAWN)
    BLACK_PAWN_3 = ("BP3", "C2", 11, RankSpec.PAWN)
    BLACK_PAWN_4 = ("BP4", "D2", 12, RankSpec.PAWN)
    BLACK_PAWN_5 = ("BP5", "E2", 13, RankSpec.PAWN)
    BLACK_PAWN_6 = ("BP6", "F2", 14, RankSpec.PAWN)
    BLACK_PAWN_7 = ("BP7", "G2", 15, RankSpec.PAWN)
    BLACK_PAWN_8 = ("BP8", "H2", 16, RankSpec.PAWN)
    
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
    def find_order_by_square(cls, square: Square) -> Optional[BlackBattleOrder]:
        for member in cls:
            if member.square_name.upper() == square.name.upper():
                return member
        return None
    
    @classmethod
    def find_order_by_piece(cls, piece: Piece) -> Optional[BlackBattleOrder]:
        """
        Finding by piece_name avoids getting a hit when searching for an opposite
        piece by mistake.
        """
        for member in cls:
            if member.piece_name.upper() == piece.name.upper():
                return member
        return None