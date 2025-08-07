from typing import List

from chess.motion.interfaces.motion_controller import MotionController
from chess.geometry.quadrant import Quadrant
from chess.motion.bishop.service.bishop_search_pattern import BishopMoveGenerator
from chess.motion.bishop.service.bishop_walk import BishopWalk



class BishopMotionController(MotionController):

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
            walk=BishopWalk(),
            search_pattern=BishopMoveGenerator(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )
