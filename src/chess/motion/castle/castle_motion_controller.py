from typing import List


from chess.motion.interfaces.motion_controller import MotionController
from chess.geometry.quadrant import Quadrant
from chess.motion.castle.service.castle_search_pattern import CastleMoveGenerator
from chess.motion.castle.castle_walk import CastleWalk


class CastleMotionController(MotionController):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant]
    ):
        super().__init__(
        name = name,
        letter = letter,
        walk = CastleWalk(),
        search_pattern = CastleMoveGenerator(),
        capture_value = capture_value,
        territories = territories,
        number_per_team = number_per_team

    )