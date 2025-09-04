from enum import Enum, auto
from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.rank.base import Rank

# class Quadrant(Enum):
#     def __new__(cls, quad_id:int, vector:Vector):
#         obj = object.__new__(cls)
#         obj._id = quad_id
#         obj._vector = vector
#
#         return obj
#
#     N = (auto(), Vector(x=0, y=1))


class RankProfile(Enum):
    def __new__(cls, letter:str, per_side:int, value:int, quadrants:List[Quadrant]):
        obj = object.__new__(cls)
        obj._letter = letter
        obj._per_side = per_side
        obj._value = value
        obj._quadrants = quadrants

        return obj

    PAWN = ("P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = ("B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    CASTLE = ("C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KING =(
        "K", 1, 0,
        [ Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    KNIGHT = ("N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    QUEEN = (
        "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )

    @property
    def letter(self) -> str:
        return self._letter


    @property
    def per_side(self) -> int:
        return self._per_side


    @property
    def value(self) -> int:
        return self._value


    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants


    def __str__(self) -> str:
        return (
            f"Rank["
            f"{self._letter} "
            f"per_team:{self._per_side} "
            f"value:{self._value} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )


    def quadrants_str(self) -> str:
        return " ".join(q.name for q in self._quadrants)


    @staticmethod
    def find_profile_by_rank(rank:Rank) -> Optional['RankProfile']:
        print(f"Looking for config with name:{rank.name}")

        for profile in RankProfile:
            print(f"Checking config:{profile.value}")
            if profile.name.upper() == rank.name.upper():
                return profile
        return None


def main():
    for profile in RankProfile:
        print(profile)


if __name__ == "__main__":
    main()





