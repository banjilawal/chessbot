from typing import List

from chess.creator.entity.builder.rank_builder import RankBuilder
from chess.rank.rank import Rank
from chess.rank.rank_spec import RankSpec


class RankFactory:

    @staticmethod
    def  assemble() -> List[Rank]:
        ranks: List[Rank] = []

        for rank_config in RankSpec:
            ranks.append(RankBuilder.build(rank_config))
        return ranks
#
# def main():
#     ranks = RankFactory.assemble()
#     for motion in ranks:
#         print(motion)
#
# if __name__ == "__main__":
#     main()