from enum import Enum
from typing import Optional

from chess.team.model.piece import ChessPiece
from chess.config.team_config import TeamConfig
from chess.config.rank_config import RankConfig


class PlacementChart(Enum):
    def __new__(
            cls,
            chess_piece_name: str,
            square_name: str,
            rank_config: RankConfig,
            team_config: TeamConfig
    ):
        obj = object.__new__(cls)
        obj._chess_piece_name= chess_piece_name
        obj._square_name = square_name
        obj._rank_config = rank_config
        obj._team_config = team_config
        return obj

    WHITE_KING_CASTLE = ("WC1", "A8", RankConfig.CASTLE, TeamConfig.WHITE)
    WHITE_KING_KNIGHT = ("WN1", "B8", RankConfig.KNIGHT, TeamConfig.WHITE)
    WHITE_KING_BISHOP = ("WB1", "C8", RankConfig.BISHOP, TeamConfig.WHITE)
    WHITE_KING = ("WK", "D8", RankConfig.QUEEN, TeamConfig.WHITE)
    WHITE_QUEEN = ("WQ", "E8", RankConfig.QUEEN, TeamConfig.WHITE)
    WHITE_QUEEN_BISHOP = ("WB2", "F8", RankConfig.BISHOP, TeamConfig.WHITE)
    WHITE_QUEEN_KNIGHT = ("WN2", "G8", RankConfig.KNIGHT, TeamConfig.WHITE)
    WHITE_QUEEN_CASTLE = ("WC2", "H8", RankConfig.CASTLE, TeamConfig.WHITE)

    WHITE_PAWN_1 = ("WP1", "A7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_2 = ("WP2", "B7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_3 = ("WP3", "C7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_4 = ("WP4", "D7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_5 = ("WP5", "E7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_6 = ("WP6", "F7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_7 = ("WP7", "G7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_8 = ("WP8", "H7", RankConfig.PAWN, TeamConfig.WHITE)

    BLACK_KING_CASTLE = ("BC1", "A1", RankConfig.CASTLE, TeamConfig.BLACK)
    BLACK_KING_KNIGHT = ("BN1", "B1", RankConfig.KNIGHT, TeamConfig.BLACK)
    BLACK_KING_BISHOP = ("BB1", "C1", RankConfig.BISHOP, TeamConfig.BLACK)
    BLACK_KING = ("BK", "D1", RankConfig.KING, TeamConfig.BLACK)
    BLACK_QUEEN = ("BQ", "E1", RankConfig.QUEEN, TeamConfig.BLACK)
    BLACK_QUEEN_BISHOP = ("BB2", "F1", RankConfig.BISHOP, TeamConfig.BLACK)
    BLACK_QUEEN_KNIGHT = ("BN2", "G1", RankConfig.KNIGHT, TeamConfig.BLACK)
    BLACK_QUEEN_CASTLE = ("BC2", "H1", RankConfig.CASTLE, TeamConfig.BLACK)

    BLACK_PAWN_1 = ("BP1", "A2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_2 = ("BP2", "B2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_3 = ("BP3", "C2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_4 = ("BP4", "D2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_5 = ("BP5", "E2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_6 = ("BP6", "F2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_7 = ("BP7", "G2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_8 = ("BP8", "H2", RankConfig.PAWN, TeamConfig.BLACK)

    @property
    def chess_piece_name(self) -> str:
        return self._chess_piece_name

    @property
    def square_name(self) -> str:
        return self._square_name

    @property
    def rank_config(self) -> RankConfig:
        return self._rank_config

    @property
    def team_config(self) -> TeamConfig:
        return self._team_config

    def map_chess_piece_to_square_name(self, chess_piece: ChessPiece) -> Optional[str]:
        # print(chess_piece.name.upper())
        if chess_piece.name.upper() == self.chess_piece_name.upper():
            return self._square_name
        return None
