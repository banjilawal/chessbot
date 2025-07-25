from enum import Enum
from typing import Optional

from chess.common.rank import PawnRank, Rank, KnightRank, BishopRank, CastleRank, QueenRank, KingRank
from chess.bishop.bishop_search_pattern import BishopSearchPattern
from chess.castle.castle_search_pattern import CastleSearchPattern
from chess.king.king_search_pattern import KingSearchPattern
from chess.knight.knight_search_pattern import KightSearchPattern
from chess.pawn.pawn_search_pattern import PawnSearchPattern
from chess.queen.queen_search_pattern import QueenSearchPattern



CAPTURE_PRIORITY = {

}

class ChessPieceConfig(Enum):
    PAWN = "Pawn"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    CASTLE = "Castle"
    QUEEN = "Queen"
    KING = "King"

    def movement_strategy(self) -> Optional[PawnSearchPattern]:
        if self == ChessPieceConfig.PAWN:
            return PawnSearchPattern()
        if self == ChessPieceConfig.KNIGHT:
            return KightSearchPattern()
        if self == ChessPieceConfig.BISHOP:
            return BishopSearchPattern()
        if self == ChessPieceConfig.CASTLE:
            return CastleSearchPattern()
        if self == ChessPieceConfig.QUEEN:
            return QueenSearchPattern()
        if self == ChessPieceConfig.KING:
            return KingSearchPattern()
        return None

    def rank(self) -> Optional[Rank]:
        if self == ChessPieceConfig.PAWN:
            return PawnRank(PawnSearchPattern())
        if self == ChessPieceConfig.KNIGHT:
            return KnightRank(KightSearchPattern())
        if self == ChessPieceConfig.BISHOP:
            return BishopRank(BishopSearchPattern())
        if self == ChessPieceConfig.CASTLE:
            return CastleRank(CastleSearchPattern())
        if self == ChessPieceConfig.QUEEN:
            return QueenRank(QueenSearchPattern())
        if self == ChessPieceConfig.KING:
            return KingRank(KingSearchPattern())
        return None

    def find_category(self, figure_rank: Rank) -> Optional['ChessPieceConfig']:
        if figure_rank == self.rank():
            return self
        return None

    def promotion_rank(self) -> Optional[Rank]:
        if self == ChessPieceConfig.PAWN or self == ChessPieceConfig.KING:
            return QueenRank(QueenSearchPattern())
        return None

    def number_per_team(self) -> int:
        if self == ChessPieceConfig.PAWN:
            return 8
        if self == ChessPieceConfig.KNIGHT:
            return 2
        if self == ChessPieceConfig.BISHOP:
            return 2
        if self == ChessPieceConfig.CASTLE:
            return 2
        if self == ChessPieceConfig.QUEEN:
            return 1
        if self == ChessPieceConfig.KING:
            return 1
        return 0



