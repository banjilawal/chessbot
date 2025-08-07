from typing import List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.motion_controller import MotionController
from chess.motion.queen.service.queen_search_pattern import QueenMoveGenerator
from chess.motion.queen.service.queen_walk import QueenWalk



class QueenMotionController(MotionController):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant]
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=QueenWalk(),
            search_pattern=QueenMoveGenerator(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )
