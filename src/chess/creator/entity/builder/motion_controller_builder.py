from chess.motion.bishop.bishop_motion_controller import BishopMotionController
from chess.motion.castle.castle_motion_controller import CastleMotionController
from chess.motion.king.king_motion_controller import KingMotionController
from chess.motion.knight.knight_motion_controller import KnightMotionController
from chess.motion.pawn.pawn_motion_controller import PawnMotionController
from chess.motion.abstract.rank_config import RankConfig
from chess.motion.queen.queen_motion_controller import QueenMotionController


class MotionControllerBuilder:

    @staticmethod
    def build(config: RankConfig):

        if config is RankConfig.KING:
            return KingMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.PAWN:
            return PawnMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.KNIGHT:
            return KnightMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.BISHOP:
            return BishopMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.CASTLE:
            return CastleMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.QUEEN:
            return QueenMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        raise ValueError(f"Invalid rank config: {config}")

#
#
# def main():
#     rank = MotionControllerBuilder.build(RankConfig.PAWN)
#     print(rank)
#
#
# if __name__ == "__main__":
#     main()