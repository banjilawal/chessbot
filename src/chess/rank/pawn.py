from typing import List


from chess.geometry.quadrant import Quadrant
from chess.rank.promote import PromotableRank
from chess.walk.pawn import PawnWalk


class PawnRank(PromotableRank):

    def __init__(
            self,
            name: str,
            letter: str,
            capture_value: int,
            number_per_team: int,
            territories: List[Quadrant],
            walk: PawnWalk = PawnWalk()
        ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

