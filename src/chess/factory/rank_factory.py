from typing import List

from chess.common.promotable import King
from chess.config.rank_config import RankConfig
from chess.rank.rank import Rank


class RankFactory:

    @staticmethod
    def run() -> List[Rank]:
        for config in RankConfig:
            print(config)
            # print(f"{config.name}, {config.capture_value}, {config.symbol}, {config.capture_value}")

    @staticmethod
    def build(config: RankConfig):
        if config == RankConfig.KING:
            return King(name=config.KING.name, value=config.capture_value)
(self, name: str, value: int, quadrants: List[Quadrant]):

def main ():
    RankFactory.build()

if __name__ == "__main__":
    main()