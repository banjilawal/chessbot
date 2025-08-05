from typing import List


from chess.motion.abstract.motion_controller import MotionController
from chess.geometry.line.quadrant import Quadrant


class CastleMotionController(MotionController):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_player: int,
        territories: List[Quadrant]
    ):
        from chess.motion.castle.service.castle_motion_service import CastleMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=CastleMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_player=number_per_player
        )
