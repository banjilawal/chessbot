from chess.creator.emit import id_emitter
from chess.creator.entity.builder.motion_controller_builder import MotionControllerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.team.model.piece import ChessPiece
from chess.motion.abstract.motion_controller import MotionController

from chess.motion.abstract.rank_config import RankConfig
from chess.config.team_config import TeamConfig
from chess.team.model.team import Team


class ChessPieceBuilder:


    @staticmethod
    def build(chess_piece_id: int, team_rank_member_id: int, motion_controller: MotionController, team: Team):

        name = team.letter.capitalize() + motion_controller.letter.capitalize() + str(team_rank_member_id)
        if motion_controller.letter == "K" or motion_controller.letter == "Q":
            name = team.letter.capitalize() + motion_controller.letter.capitalize()
        return ChessPiece(
            chess_piece_id=chess_piece_id,
            name=name,
            motion_controller=motion_controller,
            team=team
        )


def main():
    rank = MotionControllerBuilder.build(RankConfig.BISHOP)
    team = TeamBuilder.build(TeamConfig.WHITE)
    chess_piece = ChessPieceBuilder.build(id_emitter.chess_piece_id, 1, motion_controller=rank, team=team)
    print(chess_piece)

if __name__ == "__main__":
    main()