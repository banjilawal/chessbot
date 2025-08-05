from typing import List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant


if TYPE_CHECKING:
    from chess.motion.abstract.motion_controller import MotionController

from chess.motion.abstract.motion_controller import MotionController

class QueenMotionController(MotionController):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_player: int,
        territories: List[Quadrant]
    ):
        from chess.motion.queen.service.queen_motion_service import QueenMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=QueenMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_player=number_per_player
        )
