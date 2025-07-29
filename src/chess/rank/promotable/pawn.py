from typing import List

from chess.rank.promotable.promotable_rank import PromotableRank
from chess.geometry.quadrant import Quadrant


class Pawn(PromotableRank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.service.pawn_motion_service import PawnMotionService
        super().__init__(name, acronym, PawnMotionService(), capture_value, territories)
