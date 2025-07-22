from enum import Enum, auto
from typing import Optional

from chess.figure.figure_rank import PawnRank, FigureRank, KnightRank, BishopRank, CastleRank, QueenRank, KingRank
from chess.movement.movement_strategy import PawnMovement, KnightMovement, BishopMovement, CastleMovement, \
    QueenMovement, KingMovement

BOARD_DIMENSION = 8

class CheckPieceBuildConfig(Enum):
    PAWN = "Pawn"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    CASTLE = "Castle"
    QUEEN = "Queen"
    KING = "King"

    def get_movement_strategy(self) -> Optional[PawnMovement]:
        if self == CheckPieceBuildConfig.PAWN:
            return PawnMovement()
        if self == CheckPieceBuildConfig.KNIGHT:
            return KnightMovement()
        if self == CheckPieceBuildConfig.BISHOP:
            return BishopMovement()
        if self == CheckPieceBuildConfig.CASTLE:
            return CastleMovement()
        if self == CheckPieceBuildConfig.QUEEN:
            return QueenMovement()
        if self == CheckPieceBuildConfig.KING:
            return KingMovement()
        return None

    def get_figure_rank(self) -> Optional[FigureRank]:
        if self == CheckPieceBuildConfig.PAWN:
            return PawnRank(PawnMovement())
        if self == CheckPieceBuildConfig.KNIGHT:
            return KnightRank(KnightMovement())
        if self == CheckPieceBuildConfig.BISHOP:
            return BishopRank(BishopMovement())
        if self == CheckPieceBuildConfig.CASTLE:
            return CastleRank(CastleMovement())
        if self == CheckPieceBuildConfig.QUEEN:
            return QueenRank(QueenMovement())
        if self == CheckPieceBuildConfig.KING:
            return KingRank(KingMovement())
        return None

    def find_category(self, figure_rank: FigureRank) -> Optional['CheckPieceBuildConfig']:
        if figure_rank == self.get_figure_rank():
            return self
        return None

    def number_per_team(self) -> int:
        if self == CheckPieceBuildConfig.PAWN:
            return 8
        if self == CheckPieceBuildConfig.KNIGHT:
            return 2
        if self == CheckPieceBuildConfig.BISHOP:
            return 2
        if self == CheckPieceBuildConfig.CASTLE:
            return 2
        if self == CheckPieceBuildConfig.QUEEN:
            return 1
        if self == CheckPieceBuildConfig.KING:
            return 1
        return 0


