from typing import List


from chess.config.rank_config import RankConfig
from chess.rank.king import King
from chess.rank.pawn import Pawn
from chess.rank.rank import Rank


class RankFactory:

    @staticmethod
    def run() -> List[Rank]:
        for config in RankConfig:
            print(config)
            # print(f"{config.name}, {config.capture_value}, {config.acronym}, {config.capture_value}")

    @staticmethod
    def build(config: RankConfig):
        if config == RankConfig.KING:
            return King(name=config.name, capture=config.capture_value, territories=config.territories)
        elif config == RankConfig.PAWN:
            return Pawn(name=config.name, capture=config.capture_value, territories=config.territories)
        elif config == RankConfig.KNIGHT:
            return King(name=config.name, capture=config.capture_value, territories=config.territories)
        elif config == RankConfig.BISHOP:
            return Pawn(name=config.name, capture=config.capture_value, territories=config.territories)
def main ():
    RankFactory.build()

if __name__ == "__main__":
    main()