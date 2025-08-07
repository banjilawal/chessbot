from typing import List

from chess.motion.abstract.motion_controller import MotionController
from chess.geometry.quadrant import Quadrant




class BishopMotionController(MotionController):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant]
    ):
        from chess.motion.bishop.service.bishop_motion_service import BishopMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=BishopMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

