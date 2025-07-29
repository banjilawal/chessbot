from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Queen(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.service.queen_motion_service import QueenMotionService
        super().__init__(name, acronym, QueenMotionService(), capture_value, territories)
