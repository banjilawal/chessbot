from typing import Optional, List

from chess.geometry.quadrant import Quadrant
from chess.rank.queen import Queen


class PromotedQueen(Queen):
    _old_rank: Optional[str]

    def __init__(
        self,
        name: str,
        letter: str,
        value:int,
        per_side: int,
        quadrants: List[Quadrant],
        old_rank: Optional[str] = None
    ):
        super().__init__(name=name, letter=letter, value=value, per_side=per_side, quadrants=quadrants)
        _old_rank: old_rank


    @property
    def old_rank(self) -> Optional[str]:
        return self._old_rank