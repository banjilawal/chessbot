from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Knight(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.service.knight_motion_service import KnightMotionService
        super().__init__(name, acronym, KnightMotionService(), capture_value, territories)

