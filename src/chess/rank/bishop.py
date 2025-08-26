from typing import List

from chess.rank.base import Rank
from chess.geometry.quadrant import Quadrant
from chess.walk.bishop import BishopWalk


class BishopRank(Rank):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk=BishopWalk()
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )
