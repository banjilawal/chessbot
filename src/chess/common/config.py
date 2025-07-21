from enum import Enum, auto
from typing import Optional

from chess.figure.figure_rank import PawnRank, FigureRank, KnightRank, BishopRank, CastleRank, QueenRank, KingRank
from chess.movement.movement_strategy import PawnMovement, KnightMovement, BishopMovement, CastleMovement, \
    QueenMovement, KingMovement

BOARD_DIMENSION = 8

class ChessFigureCategory(Enum):
    PAWN = "Pawn"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    CASTLE = "Castle"
    QUEEN = "Queen"
    KING = "King"

    def get_figure_rank(self) -> Optional[FigureRank]:
        if self == ChessFigureCategory.PAWN:
            return PawnRank(PawnMovement())
        if self == ChessFigureCategory.KNIGHT:
            return KnightRank(KnightMovement())
        if self == ChessFigureCategory.BISHOP:
            return BishopRank(BishopMovement())
        if self == ChessFigureCategory.CASTLE:
            return CastleRank(CastleMovement())
        if self == ChessFigureCategory.QUEEN:
            return QueenRank(QueenMovement())
        if self == ChessFigureCategory.KING:
            return KingRank(KingMovement())
        return None

    def find_category(self, figure_rank: FigureRank) -> Optional['ChessFigureCategory']:
        if figure_rank == self.get_figure_rank():
            return self
        return None


