# chess/rank/spec.py

"""
Module: chess.rank.spec
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from enum import Enum, auto
from chess.geometry import Quadrant


class RankSpec(Enum):
    
    def __new__(cls, id: int, letter: str, quota: int, ransom: int, quadrants: List[Quadrant]):
        obj = object.__new__(cls)
        obj._id = id
        obj._letter = letter
        obj._quota = quota
        obj._ransom = ransom
        obj._quadrants = quadrants
        
        return obj
    
    PAWN = (1, "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = (2, "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    ROOK = (3, "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KNIGHT = (4,"N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    
    KING = (
        5, "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    
    QUEEN = (
        6, "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    
    @property
    def id(self) -> int:
        return self._id
    
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
            f"{self._id} "
            f"{self._letter} "
            f"per_team:{self._quota} "
            f"value:{self._ransom} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )
    
    def quadrants_str(self) -> str:
        return " ".join(q.visitor_name for q in self._quadrants)
    
    def valid_ranks(self):
        return
    
    @property
    def max_rank_id(self) -> int:
        return RankSpec.QUEEN.id
    
    @classmethod
    def find_speck_by_rank(cls, rank: Rank) -> Optional[RankSpec]:
        print(f"Looking for config with name:{rank.visitor_name}")
        
        for spec in RankSpec:
            print(f"Checking config:{spec.ransom}")
            if spec.name.upper() == rank.visitor_name.upper():
                return spec
        return None
