from typing import List

from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.motion_controller import MotionController


class KingMotionController(MotionController):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant]
    ):
        from chess.motion.king.service.king_motion_service import KingMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=KingMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

