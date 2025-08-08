from enum import Enum
from typing import List

from chess.geometry.quadrant import Quadrant
from chess.rank.rank import Rank


class RankConfig(Enum):
    def __new__(
        cls,
        name: str,
        letter,
        number_per_player: int,
        capture_value: int,
        territories: List[Quadrant]
    ):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._letter = letter
        obj._number_per_player = number_per_player
        obj._capture_value = capture_value
        obj._territories = territories
        return obj

    PAWN = ("PawnRank", "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = ("BishopRank", "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    CASTLE = ("CastleRank", "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KING =(
        "KingRank", "K", 1, 0,
        [
            Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE,
            Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW
        ]
    )
    KNIGHT = (
        "KnightRank", "N", 2, 3,
        [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW]
    )
    QUEEN = (
        "Queen", "Q", 1, 9,
        [
            Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE,
            Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW
        ]
    )

    @property
    def letter(self) -> str:
        return self._letter

    @property
    def number_per_player(self) -> int:
        return self._number_per_player

    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories

    @staticmethod
    def find_config_by_class(rank: Rank) -> "RankConfig":
        print(f"Looking for config with name: {rank.name}")
        for config in RankConfig:
            print(f"Checking config: {config.value}")
            if config.value.upper() == rank.name.upper():
                return config
        return None


