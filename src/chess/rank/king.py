from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class King(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.king_motion import KingMotionService
        super().__init__(name, acronym, KingMotionService(), capture_value, territories)
