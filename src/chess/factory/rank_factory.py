from typing import List

from chess.factory.builder.rank_builder import RankBuilder
from chess.rank.rank import Rank
from chess.rank.rank_config import RankConfig


class RankFactory:

    @staticmethod
    def  assemble() -> List[Rank]:
        ranks: List[Rank] = []

        for rank_config in RankConfig:
            ranks.append(RankBuilder.build(rank_config))
        return ranks

def main():
    ranks = RankFactory.assemble()
    for rank in ranks:
        print(rank)

if __name__ == "__main__":
    main()