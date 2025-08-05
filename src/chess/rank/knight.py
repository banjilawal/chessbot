from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Knight(Rank):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_player: int,
        territories: List[Quadrant]
    ):
        from chess.motion.service.knight_motion_service import KnightMotionService
        super().__init__(
            name=name,
            letter=letter,
            motion_service=KnightMotionService(),
            capture_value=capture_value,
            territories=territories,
            number_per_player=number_per_player
        )


