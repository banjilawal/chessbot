from chess.rank.bishop import Bishop
from chess.rank.castle import Castle
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.rank.pawn import Pawn
from chess.config.rank import RankProfile
from chess.rank.queen import Queen


class RankBuilder:

    @staticmethod
    def build(config: RankProfile):

        if config is RankProfile.KING:
            return King(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        if config is RankProfile.PAWN:
            return Pawn(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        if config is RankProfile.KNIGHT:
            return Knight(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        if config is RankProfile.BISHOP:
            return Bishop(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        if config is RankProfile.CASTLE:
            return Castle(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        if config is RankProfile.QUEEN:
            return Queen(
                name=config.name,
                letter=config.letter,
                per_team=config.number_per_team,
                territories=config.territories,
                value=config.capture_value
            )
        raise ValueError(f"Invalid rank config: {config}")



def main():
    rank = RankBuilder.build(RankProfile.PAWN)
    print(rank)


if __name__ == "__main__":
    main()