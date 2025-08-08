from typing import List

from chess.geometry.quadrant import Quadrant
from chess.motion.controller.motion_controller import MotionController
from chess.motion.walk.queen_walk import QueenWalk



class QueenMotionController(MotionController):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk=QueenWalk()
        # explorer=QueenExplorer()
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            explorer=explorer,
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )
