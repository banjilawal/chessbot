from chess.rank.bishop import BishopRank
from chess.rank.castle import CastleRank
from chess.rank.king import KingRank
from chess.rank.knight import KnightRank
from chess.rank.pawn import PawnRank
from chess.config.rank import RankConfig
from chess.rank.queen import QueenRank


class RankBuilder:

    @staticmethod
    def build(config: RankConfig):

        if config is RankConfig.KING:
            return KingRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.PAWN:
            return PawnRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.KNIGHT:
            return KnightRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.BISHOP:
            return BishopRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.CASTLE:
            return CastleRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        if config is RankConfig.QUEEN:
            return QueenRank(
                name=config.name,
                letter=config.letter,
                number_per_team=config.number_per_team,
                territories=config.territories,
                capture_value=config.capture_value
            )
        raise ValueError(f"Invalid rank config: {config}")



def main():
    rank = RankBuilder.build(RankConfig.PAWN)
    print(rank)


if __name__ == "__main__":
    main()