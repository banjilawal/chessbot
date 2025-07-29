from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Queen(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.queen_motion import QueenMotion
        super().__init__(name, acronym, QueenMotion, capture_value, territories)
