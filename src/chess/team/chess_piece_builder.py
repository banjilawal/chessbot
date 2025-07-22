from chess.common.config import CheckPieceBuildConfig
from chess.figure.chess_piece import ChessPiece
from chess.figure.figure_rank import KingRank, QueenRank, CastleRank, BishopRank, KnightRank, PawnRank
from chess.movement.movement_strategy import KingMovement, QueenMovement, CastleMovement, KnightMovement, \
    BishopMovement, PawnMovement
from chess.team.team import Team


class ChessPieceBuilder:

    def create(chess_piece_id: int, team: Team, category: CheckPieceBuildConfig):
        name = team.color + "_" + category
        figure_rank = None
        number_of_rank_members = 0

        if category == CheckPieceBuildConfig.KING:
            figure_rank = KingRank(KingMovement());
            number_of_rank_members = 1

        if category == CheckPieceBuildConfig.QUEEN:
            figure_rank= QueenRank(QueenMovement())
            number_of_rank_members = 1

        if category == CheckPieceBuildConfig.CASTLE:
            figure_rank = CastleRank(CastleMovement())
            number_of_rank_members = 2

        if category == CheckPieceBuildConfig.BISHOP:
            figure_rank = BishopRank(BishopMovement())
            number_of_rank_members = 2

        if category == CheckPieceBuildConfig.KNIGHT:
            figure_rank = KnightRank(KnightMovement())
            number_of_rank_members = 2

        if category == CheckPieceBuildConfig.PAWN:
            figure_rank = PawnRank(PawnMovement())
            number_of_rank_members = 8
        self.add_team_members(figure=figure_rank, number_of_rank_members=number_of_rank_members, team=team)

    def add_team_members(self, chess_figure_category: CheckPieceBuildConfig, chess_rank: ChessRank,
                         Ch, number_of_rank_members, team):
        inner_dict = dict()
        team.piece_registry[chess_rank.name] = dict()