from typing import List


from chess.geometry.quadrant import Quadrant
from chess.motion.interfaces.motion_controller import MotionController
from chess.motion.pawn.service.pawn_search_pattern import PawnMoveGenerator
from chess.motion.pawn.pawn_walk import PawnWalk


class PawnMotionController(MotionController):

    def __init__(
            self,
            name: str,
            letter: str,
            capture_value: int,
            number_per_team: int,
            territories: List[Quadrant]
        ):
        super().__init__(
            name=name,
            letter=letter,
            walk=PawnWalk(),
            search_pattern=PawnMoveGenerator(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

