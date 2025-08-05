from typing import List

from chess.factory.builder.rank_builder import RankBuilder
from chess.motion.abstract.motion_controller import MotionController
from chess.motion.abstract.rank_config import RankConfig


class RankFactory:

    @staticmethod
    def  assemble() -> List[MotionController]:
        ranks: List[MotionController] = []

        for rank_config in RankConfig:
            ranks.append(RankBuilder.build(rank_config))
        return ranks

def main():
    ranks = RankFactory.assemble()
    for rank in ranks:
        print(rank)

if __name__ == "__main__":
    main()