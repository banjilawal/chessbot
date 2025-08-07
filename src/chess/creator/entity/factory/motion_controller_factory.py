from typing import List

from chess.creator.entity.builder.motion_controller_builder import MotionControllerBuilder
from chess.motion.interfaces.motion_controller import MotionController
from chess.motion.interfaces.rank_config import RankConfig


class MotionControllerFactory:

    @staticmethod
    def  assemble() -> List[MotionController]:
        motion_controllers: List[MotionController] = []

        for rank_config in RankConfig:
            motion_controllers.append(MotionControllerBuilder.build(rank_config))
        return motion_controllers

# def main():
#     ranks = MotionControllerFactory.assemble()
#     for rank in ranks:
#         print(rank)
#
# if __name__ == "__main__":
#     main()