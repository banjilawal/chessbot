from typing import List

from chess.geometry.quadrant import Quadrant
from chess.rank.promotable.promotable_rank import PromotableRank
from chess.rank.walk.king_walk import KingWalk


class KingRank(PromotableRank):
    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk=KingWalk()
        # explorer=KingExplorer()
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            # explorer=explorer,
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )
