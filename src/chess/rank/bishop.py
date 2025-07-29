from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant




class Bishop(Rank):
    """Bishop rank implementation that inherits from Rank."""

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):

        from chess.motion.bishop_motion import BishopMotionService
        super().__init__(name, acronym, BishopMotionService(), capture_value, territories)

