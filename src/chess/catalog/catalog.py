# src/chess/catalog/catalog.py

"""
Module: chess.catalog.catalog
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from enum import Enum
from typing import List, Optional

from chess.geometry import Quadrant
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankSpec, Rook


class Catalog(Enum):
    """
    # ROLE: Configuration

    # RESPONSIBILITIES:
    1.  Catalog of settings for each concrete Rank

    # PROVIDES:
    Enum

    # ATTRIBUTES:

    """
    
    def __new__(cls, designation: str, team_quota: int, ransom: int, quadrants: List[Quadrant]):
        """
        Factory method for creating new instances of Catalog enum.
        """
        obj = object.__new__(cls)
        obj._designation = designation
        obj._team_quota = team_quota
        obj._ransom = ransom
        obj._quadrants = quadrants
        
        return obj
    
    PAWN = ("P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW])
    BISHOP = ("B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW])
    ROOK = ("C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W])
    KNIGHT = ("N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW])
    
    KING = (
        "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    
    QUEEN = (
        "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW]
    )
    
    @property
    def designation(self) -> str:
        return self._designation
    
    @property
    def quota(self) -> int:
        return self._team_quota
    
    @property
    def ransom(self) -> int:
        return self._ransom
    
    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants
    
    @classmethod
    def allowed_quadrants(cls) -> List[List[Quadrant]]:
        return [member.quadrants for member in cls]
    
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
        return " ".join(q.name for q in self._quadrants)

    # @classmethod
    # def find_speck_by_rank(cls, rank: Rank) -> Optional[Catalog]:
    #     print(f"Looking for config with designation:{rank.visitor_name}")
    #
    #     for spec in Catalog:
    #         print(f"Checking config:{spec.ransom}")
    #         if spec.designation.upper() == rank.visitor_name.upper():
    #             return spec
    #     return None
