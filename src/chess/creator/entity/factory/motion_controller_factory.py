from typing import List

from chess.creator.entity.builder.motion_controller_builder import MotionControllerBuilder
from chess.rank.rank import Rank
from chess.config.rank_config import RankConfig


class MotionControllerFactory:

    @staticmethod
    def  assemble() -> List[Rank]:
        motion_controllers: List[Rank] = []

        for rank_config in RankConfig:
            motion_controllers.append(MotionControllerBuilder.build(rank_config))
        return motion_controllers

# def main():
#     ranks = MotionControllerFactory.assemble()
#     for motion in ranks:
#         print(motion)
#
# if __name__ == "__main__":
#     main()