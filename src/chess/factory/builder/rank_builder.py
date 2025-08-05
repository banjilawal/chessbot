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
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.PAWN:
            return Pawn(
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.KNIGHT:
            return Knight(
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.BISHOP:
            return Bishop(
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.CASTLE:
            return Castle(
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        if config is RankConfig.QUEEN:
            return Queen(
                name=config.name,
                letter=config.letter,
                number_per_player=config.number_per_player,
                territories=config.territories,
                capture_value=config.capture_value,
            )
        raise ValueError(f"Invalid rank config: {config}")



def main():
    rank = RankBuilder.build(RankConfig.PAWN)
    print(rank)


if __name__ == "__main__":
    main()