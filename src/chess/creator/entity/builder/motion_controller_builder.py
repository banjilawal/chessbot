from chess.rank.bishop_rank import BishopMotionController
from chess.rank.castle_rank import CastleMotionController
from chess.rank.promotable.king_rank import KingRank
from chess.rank.knight_rank import KnightMotionController
from chess.rank.promotable.pawn_rank import PawnRank
from chess.config.rank_config import RankConfig
from chess.rank.queen_rank import QueenMotionController


class MotionControllerBuilder:

    @staticmethod
    def build(config: RankConfig):

        if config is RankConfig.KING:
            return KingRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.PAWN:
            return PawnRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.KNIGHT:
            return KnightMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.BISHOP:
            return BishopMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.CASTLE:
            return CastleMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.QUEEN:
            return QueenMotionController(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value
            )
        raise ValueError(f"Invalid rank config: {config}")

#
#
# def main():
#     motion = MotionControllerBuilder.build(RankConfig.PAWN)
#     print(motion)
#
#
# if __name__ == "__main__":
#     main()