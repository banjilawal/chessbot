from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Castle(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):

        from chess.motion.castle_motion import CastleMotionService
        super().__init__(name, acronym, CastleMotionService(), capture_value, territories)
