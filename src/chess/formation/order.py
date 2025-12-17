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
from chess.team import BlackBattleOrder


class BattleOrder(Enum):
    def __new__(
            cls,
            color: GameColor,
            piece_name: str,
            square_name: str,
            roster_number: int,
            rank_spec: RankSpec,
    ):
        obj = object.__new__(cls)
        obj._color = color
        obj._piece_name = piece_name
        obj._square_name = square_name
        obj._roster_number = roster_number
        obj._rank_spec = rank_spec
        return obj
    
    BLACK_KING_CASTLE = ("BC1", "A1", GameColor.BLACK, 1, RankSpec.ROOK)
    BLACK_KING_KNIGHT = ("BN1", "B1", GameColor.BLACK, 2, RankSpec.KNIGHT)
    BLACK_KING_BISHOP = ("BB1", "C1", GameColor.BLACK, 3, RankSpec.BISHOP)
    BLACK_KING = ("BK", "D1", GameColor.BLACK, 4, RankSpec.KING)
    BLACK_QUEEN = ("BQ", "E1", GameColor.BLACK, 5, RankSpec.QUEEN)
    BLACK_QUEEN_BISHOP = ("BB2", "F1", GameColor.BLACK, 6, RankSpec.BISHOP)
    BLACK_QUEEN_KNIGHT = ("BN2", "G1", GameColor.BLACK, 7, RankSpec.KNIGHT)
    BLACK_QUEEN_CASTLE = ("BC2", "H1", GameColor.BLACK, 8, RankSpec.ROOK)
    
    BLACK_PAWN_1 = ("BP1", "A2", GameColor.BLACK, 9, RankSpec.PAWN)
    BLACK_PAWN_2 = ("BP2", "B2", GameColor.BLACK, 10, RankSpec.PAWN)
    BLACK_PAWN_3 = ("BP3", "C2", GameColor.BLACK, 11, RankSpec.PAWN)
    BLACK_PAWN_4 = ("BP4", "D2", GameColor.BLACK, 12, RankSpec.PAWN)
    BLACK_PAWN_5 = ("BP5", "E2", GameColor.BLACK, 13, RankSpec.PAWN)
    BLACK_PAWN_6 = ("BP6", "F2", GameColor.BLACK, 14, RankSpec.PAWN)
    BLACK_PAWN_7 = ("BP7", "G2", GameColor.BLACK, 15, RankSpec.PAWN)
    BLACK_PAWN_8 = ("BP8", "H2", GameColor.BLACK, 16, RankSpec.PAWN)
    
    WHITE_KING_CASTLE = ("WC1", "A8", GameColor.WHITE, 1, RankSpec.ROOK)
    WHITE_KING_KNIGHT = ("WN1", "B8", GameColor.WHITE, 2, RankSpec.KNIGHT)
    WHITE_KING_BISHOP = ("WB1", "C8", GameColor.WHITE, 3, RankSpec.BISHOP)
    WHITE_KING = ("WK", "D8", GameColor.WHITE, 4, RankSpec.KING)
    WHITE_QUEEN = ("WQ", "E8", GameColor.WHITE, 5, RankSpec.QUEEN)
    WHITE_QUEEN_BISHOP = ("WB2", GameColor.WHITE, 6, "F8", RankSpec.BISHOP)
    WHITE_QUEEN_KNIGHT = ("WN2", GameColor.WHITE, 7, "G8", RankSpec.KNIGHT)
    WHITE_QUEEN_CASTLE = ("WC2", GameColor.WHITE, 8, "H8", RankSpec.ROOK)
    
    WHITE_PAWN_1 = ("WP1", "A7", GameColor.WHITE, 9, RankSpec.PAWN)
    WHITE_PAWN_2 = ("WP2", "B7", GameColor.WHITE, 10, RankSpec.PAWN)
    WHITE_PAWN_3 = ("WP3", "C7", GameColor.WHITE, 11, RankSpec.PAWN)
    WHITE_PAWN_4 = ("WP4", "D7", GameColor.WHITE, 12, RankSpec.PAWN)
    WHITE_PAWN_5 = ("WP5", "E7", GameColor.WHITE, 13, RankSpec.PAWN)
    WHITE_PAWN_6 = ("WP6", "F7", GameColor.WHITE, 14, RankSpec.PAWN)
    WHITE_PAWN_7 = ("WP7", "G7", GameColor.WHITE, 15, RankSpec.PAWN)
    WHITE_PAWN_8 = ("WP8", "H7", GameColor.WHITE, 16, RankSpec.PAWN)
    
    @property
    def piece_name(self) -> str:
        return self._piece_name
    
    @property
    def square(self) -> str:
        return self._square_name
    
    @property
    def rank_spec(self) -> RankSpec:
        return self._rank_spec
    
    @property
    def roster_number(self) -> int:
        return self._roster_number
    
    @property
    def color(self) -> GameColor:
        return self._color
    
    @classmethod
    def allowed_roster_numbers(cls) -> List[int]:
        return [member.roster_number for member in cls]
    
    @classmethod
    def upper_case_piece_names(cls) -> List[str]:
        return [member.piece_name.upper() for member in cls]
    
    @classmethod
    def upper_case_square_names(cls) -> List[str]:
        return [member.square.upper() for member in cls]
    
    @classmethod
    def find_order_by_square(cls, square: Square) -> Optional[BlackBattleOrder]:
        for member in cls:
            if member.square.upper() == square.name.upper():
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