from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Pawn(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.pawn_motion import PawnMotionService
        super().__init__(name, acronym, PawnMotionService(), capture_value, territories)
