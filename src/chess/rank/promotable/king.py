from typing import List

from chess.rank.promotable.promotable_rank import PromotableRank
from chess.geometry.quadrant import Quadrant


class King(PromotableRank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.service.king_motion_service import KingMotionService
        super().__init__(name, acronym, KingMotionService(), capture_value, territories)
