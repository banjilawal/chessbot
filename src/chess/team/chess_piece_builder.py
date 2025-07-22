from chess.common.config import ChessPieceConfig
from chess.figure.chess_piece import ChessPiece
from chess.figure.figure_rank import KingRank, QueenRank, CastleRank, BishopRank, KnightRank, PawnRank
from chess.movement.movement_strategy import KingMovement, QueenMovement, CastleMovement, KnightMovement, \
    BishopMovement, PawnMovement
from chess.team.team import Team


class ChessPieceBuilder:

    def create(chess_piece_id:int, team:Team, buildConfig:ChessPieceConfig):
        name = team.color + "_" + buildConfig.name

        if



    def add_team_members(self, chess_figure_category: ChessPieceConfig, chess_rank: ChessRank,
                         Ch, number_of_rank_members, team):
        inner_dict = dict()
        team.piece_registry[chess_rank.name] = dict()