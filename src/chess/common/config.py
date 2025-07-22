from enum import Enum, auto
from typing import Optional

from chess.figure.figure_rank import PawnRank, FigureRank, KnightRank, BishopRank, CastleRank, QueenRank, KingRank
from chess.motion.movement_strategy import PawnMovement, KnightMovement, BishopMovement, CastleMovement, \
    QueenMovement, KingMovement

BOARD_DIMENSION = 8

class ChessPieceConfig(Enum):
    PAWN = "Pawn"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    CASTLE = "Castle"
    QUEEN = "Queen"
    KING = "King"

    def movement_strategy(self) -> Optional[PawnMovement]:
        if self == ChessPieceConfig.PAWN:
            return PawnMovement()
        if self == ChessPieceConfig.KNIGHT:
            return KnightMovement()
        if self == ChessPieceConfig.BISHOP:
            return BishopMovement()
        if self == ChessPieceConfig.CASTLE:
            return CastleMovement()
        if self == ChessPieceConfig.QUEEN:
            return QueenMovement()
        if self == ChessPieceConfig.KING:
            return KingMovement()
        return None

    def rank(self) -> Optional[FigureRank]:
        if self == ChessPieceConfig.PAWN:
            return PawnRank(PawnMovement())
        if self == ChessPieceConfig.KNIGHT:
            return KnightRank(KnightMovement())
        if self == ChessPieceConfig.BISHOP:
            return BishopRank(BishopMovement())
        if self == ChessPieceConfig.CASTLE:
            return CastleRank(CastleMovement())
        if self == ChessPieceConfig.QUEEN:
            return QueenRank(QueenMovement())
        if self == ChessPieceConfig.KING:
            return KingRank(KingMovement())
        return None

    def find_category(self, figure_rank: FigureRank) -> Optional['ChessPieceConfig']:
        if figure_rank == self.rank():
            return self
        return None

    def promotion_rank(self) -> Optional[FigureRank]:
        if self == ChessPieceConfig.PAWN or self == ChessPieceConfig.KING:
            return QueenRank(QueenMovement())
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



