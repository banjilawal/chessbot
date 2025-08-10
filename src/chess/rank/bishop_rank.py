from typing import List

from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant
from chess.walk import BishopWalk



class BishopRank(Rank):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk=BishopWalk()
        # explorer=BishopExplorer(),
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
