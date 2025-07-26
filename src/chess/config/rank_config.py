from enum import Enum
from chess.geometry.quadrant import Quadrant


class RankConfig(Enum):
    def __new__(cls, name: str, acronym, number_per_player: int, capture_value: int, territories: [Quadrant]):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._acronym = acronym
        obj._number_per_player = number_per_player
        obj._capture_value = capture_value
        obj._territories = territories
        return obj

    KING =(
        "king", "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S,  Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    PAWN = ("pawn", "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    KNIGHT = ("knight", "N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    BISHOP = ("bishop", "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    CASTLE = ("castle", "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    QUEEN = (
        "queen", "Q", 1, 9,
         [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
     )

    @property
    def acronym(self) -> str:
        return self._acronym

    @property
    def number_per_player(self) -> int:
        return self._number_per_player

    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> [Quadrant]:
        return self._territories.copy()
from enum import Enum
from typing import List
