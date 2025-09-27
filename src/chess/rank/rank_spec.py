from enum import Enum, auto
from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.rank.rank import Rank

# class Quadrant(Enum):
#     def __new__(cls, quad_id:int, null-pkg:Vector):
#         obj = object.__new__(cls)
#         obj._id = quad_id
#         obj._vector = null-pkg
#
#         return obj
#
#     N = (auto(), Vector(x=0, y=1))


class RankSpec(Enum):
    def __new__(cls, letter:str, quota:int, ransom:int, quadrants:List[Quadrant]):
        obj = object.__new__(cls)
        obj._letter = letter
        obj._quota = quota
        obj._ransom = ransom
        obj._quadrants = quadrants

        return obj

    PAWN = ("P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = ("B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    ROOK = ("C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KNIGHT = ("N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])

    KING =(
        "K", 1, 0,
        [ Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )

    QUEEN = (
        "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )

    @property
    def letter(self) -> str:
        return self._letter


    @property
    def quota(self) -> int:
        return self._quota


    @property
    def ransom(self) -> int:
        return self._ransom


    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants


    def __str__(self) -> str:
        return (
            f"Rank["
            f"{self._letter} "
            f"per_team:{self._quota} "
            f"value:{self._ransom} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )


    def quadrants_str(self) -> str:
        return " ".join(q.name for q in self._quadrants)


    @staticmethod
    def find_speck_by_rank(rank: Rank) -> Optional['RankSpec']:
        print(f"Looking for config with name:{rank.name}")

        for spec in RankSpec:
            print(f"Checking config:{spec.ransom}")
            if spec.name.upper() == rank.name.upper():
                return spec
        return None


def main():
    for spec in RankSpec:
        print(spec)


if __name__ == "__main__":
    main()





