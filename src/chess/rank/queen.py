from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.rank.base import Rank
from chess.rank.promote import PromotableRank
from chess.walk.queen import QueenWalk


class QueenRank(Rank):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk=QueenWalk()
        # explorer=QueenExplorer()
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

class PromotedQueen(QueenRank):
    _old_rank: Optional[PromotableRank]

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:int,
        number_per_team: int,
        territories: List[Quadrant],
        walk=QueenWalk(),
        old_rank: Optional[PromotableRank] = None
    ):
        super().__init__(name, letter, capture_value, number_per_team, territories, walk)
        _old_rank: old_rank


    @property
    def old_rank(self) -> Optional[PromotableRank]:
        return self._old_rank




