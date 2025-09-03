from enum import Enum
from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.rank.base import Rank


class RankProfile(Enum):
    def __new__(
        cls,
        letter,
        number_per_team: int,
        capture_value: int,
        territories: List[Quadrant]
    ):
        obj = object.__new__(cls)
        obj._letter = letter
        obj._per_team = number_per_team
        obj._value = capture_value
        obj._territories = territories
        return obj

    PAWN = ("P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = ("B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    CASTLE = ("C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KING =(
        "K", 1, 0,
        [ Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    KNIGHT = ( "N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    QUEEN = (
        "Queen", "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )

    @property
    def letter(self) -> str:
        return self._letter

    @property
    def number_per_team(self) -> int:
        return self._per_team

    @property
    def capture_value(self) -> int:
        return self._value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories


    def __str__(self) -> str:
        return (
            f"letter:{self._letter}, "
            f"per_team:{self._per_team} "
            f"value:{self._value} "
            f"side:{self._side}"
            f"[{self._quadrants_str()}]"
            f"] "
        )


    def _quadrants_str(self) -> str:
        names = f"["
        for quadrant in self._territories:
            names += f"quadrant.name "

        return names.strip() + f"]"


    @staticmethod
    def find_profile_by_rank(rank: Rank) -> Optional['RankProfile']:
        print(f"Looking for config with name: {rank.name}")

        for profile in RankProfile:
            print(f"Checking config: {profile.value}")
            if profile.name.upper() == rank.name.upper():
                return profile
        return None


def main(self):
    for profile in RankProfile:
        print(profile)


if __name__ == "__main__":
    main()





