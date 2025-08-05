from chess.factory.builder.rank_builder import RankBuilder
from chess.factory.builder.team_builder import TeamBuilder
from chess.factory.emit import id_emitter

from chess.piece.piece import ChessPiece
from chess.motion.motion_controller import MotionController

from chess.rank.rank_config import RankConfig
from chess.team.team import Team
from chess.team.team_config import TeamConfig

# if TYPE_CHECKING:
#     from chess.rank.rank import MotionController


class ChessPieceBuilder:


    @staticmethod
    def build(chess_piece_id: int, team_rank_member_id: int, rank: MotionController, team: Team):
        name = team.letter.capitalize() + rank.letter.capitalize() + str(team_rank_member_id)
        if rank.letter == "K" or rank.letter == "Q":
            name = team.letter.capitalize() + rank.letter.capitalize()
        return ChessPiece(
            chess_piece_id=chess_piece_id,
            name=name,
            rank=MotionController,
            team=team
        )


def main():
    rank = RankBuilder.build(RankConfig.BISHOP)
    team = TeamBuilder.build(TeamConfig.WHITE)
    chess_piece = ChessPieceBuilder.build(id_emitter.chess_piece_id, 1, rank=rank, team=team)
    print(chess_piece)

if __name__ == "__main__":
    main()