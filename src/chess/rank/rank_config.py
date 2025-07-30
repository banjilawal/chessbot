from enum import Enum
from chess.geometry.quadrant import Quadrant
from chess.rank.rank import Rank


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
        "King", "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W,Quadrant.NW]
    )
    PAWN = ("Pawn", "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    KNIGHT = ("Knight", "N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    BISHOP = ("Bishop", "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    CASTLE = ("Castle", "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    QUEEN = (
        "Queen", "Q", 1, 9,
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

    @staticmethod
    def find_config_by_class(rank: Rank):
        print(f"Looking for config with name: {rank.name}")
        for config in RankConfig:
            print(f"Checking config: {config.value}")
            if config.value.upper() == rank.name.upper():
                return config
        return None


