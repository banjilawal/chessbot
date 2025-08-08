from typing import List


from chess.geometry.quadrant import Quadrant
from chess.motion.controller.promotable.promotable_rank import PromotableRank
from chess.motion.walk.pawn_walk import PawnWalk


class PawnMotionController(PromotableRank):

    def __init__(
            self,
            name: str,
            letter: str,
            capture_value: int,
            number_per_team: int,
            territories: List[Quadrant],
            walk: PawnWalk()
            # explorer: PawnExplorer
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

