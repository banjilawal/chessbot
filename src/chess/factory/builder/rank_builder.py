from chess.rank.bishop import Bishop
from chess.rank.castle import Castle
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.rank.pawn import Pawn
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.rank.rank_config import RankConfig


class RankBuilder:

    @staticmethod
    def build(config: RankConfig):

        if config is RankConfig.KING:
            return King(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )
        if config is RankConfig.PAWN:
            return Pawn(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )
        if config is RankConfig.KNIGHT:
            return Knight(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )
        if config is RankConfig.BISHOP:
            return Bishop(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )
        if config is RankConfig.CASTLE:
            return Castle(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )
        if config is RankConfig.QUEEN:
            return Queen(
                config.name,
                config.letter,
                config.number_per_player,
                config.territories,
                config.capture_value,
                config.motion_service
            )



def main():
    rank = RankBuilder.build(RankConfig.PAWN)


if __name__ == "__main__":
    main()