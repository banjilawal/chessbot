from enum import Enum
from typing import List

from chess.config.rank_config import RankConfig
from chess.geometry.quadrant import Quadrant


class RankValue(Enum):
    KING = 0
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3
    CASTLE = 5
    QUEEN = 5

    @property
    def value(self) -> int:
        return self.value

    @property
    def name(self) -> str:
        return self.name

    @property
    def quadrants(self) -> List[Quadrant]:
        if self == RankConfig.KING:
            return [
                Quadrant.N, Quadrant.NE, Quadrant.NW,
                Quadrant.E, Quadrant.SE, Quadrant.SW,
                Quadrant.W, Quadrant.S
            ]
        if self == RankConfig.PAWN:
            return [Quadrant.N, Quadrant.NE, Quadrant.NW]
        if self == RankConfig.KNIGHT:
            return [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW]
        if self == RankConfig.BISHOP:
            return [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW]
        if self == RankConfig.CASTLE:
            return [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W]
        if self == RankConfig.QUEEN:
            return [
                Quadrant.N, Quadrant.NE, Quadrant.NW,
                Quadrant.E, Quadrant.SE, Quadrant.SW,
                Quadrant.W, Quadrant.S
            ]
        return []
