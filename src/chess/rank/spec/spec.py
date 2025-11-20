# src/chess/rank/spec/spec.py

"""
Module: chess.rank.spec.spec
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""

from enum import Enum
from typing import List

from chess.geometry import Quadrant


class RankSpec(Enum):
    """
    # ROLE: Configuration

    # RESPONSIBILITIES:
    1.  Catalog of settings for each concrete Rank

    # PROVIDES:
    Enum

    # ATTRIBUTES:
        *   id (int):           Identifier for the subclass.
        *   name (str):         Common name of the rank.
        *   designation (str):  Chess designation
        *   ransom (int):       Value of ranks that can be captured.
        *   team_quota  (int):  Number of instances on a team.
        *   quadrants (List[Quadrant]):
    """
    
    def __new__(cls, id: int, designation: str, team_quota: int, ransom: int, quadrants: List[Quadrant]):
        """
        Factory method for creating new instances of RankSpec enum.
        """
        obj = object.__new__(cls)
        obj._id = id
        obj._designation = designation
        obj._team_quota = team_quota
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
    def designation(self) -> str:
        return self._designation
    
    @property
    def team_quota(self) -> int:
        return self._team_quota
    
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
            f"{self._designation} "
            f"per_team:{self._team_quota} "
            f"value:{self._ransom} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )
    
    def quadrants_str(self) -> str:
        return " ".join(q.visitor_name for q in self._quadrants)

    
    @property
    def max_rank_id(self) -> int:
        return RankSpec.QUEEN.id
    
    # @classmethod
    # def find_speck_by_rank(cls, rank: Rank) -> Optional[RankSpec]:
    #     print(f"Looking for config with name:{rank.visitor_name}")
    #
    #     for spec in RankSpec:
    #         print(f"Checking config:{spec.ransom}")
    #         if spec.name.upper() == rank.visitor_name.upper():
    #             return spec
    #     return None
