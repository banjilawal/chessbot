from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant


class Knight(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.knight_motion import KnightMotion
        super().__init__(name, acronym, KnightMotion, capture_value, territories)

