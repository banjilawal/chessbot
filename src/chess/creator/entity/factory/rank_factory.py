from typing import List

from chess.creator.entity.builder.rank_builder import RankBuilder
from chess.rank.rank import Rank
from chess.config.rank_config import RankConfig


class RankFactory:

    @staticmethod
    def  assemble() -> List[Rank]:
        motion_controllers: List[Rank] = []

        for rank_config in RankConfig:
            motion_controllers.append(RankBuilder.build(rank_config))
        return motion_controllers

def main():
    ranks = RankFactory.assemble()
    for motion in ranks:
        print(motion)

if __name__ == "__main__":
    main()