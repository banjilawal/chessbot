from typing import List


from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.motion_controller import MotionController


class PawnMotionController(MotionController):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_player: int,
        territories: List[Quadrant]
    ):
        from chess.motion.pawn.service.pawn_motion_service import PawnMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=PawnMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_player=number_per_player
        )

