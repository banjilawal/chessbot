# src/chess/persona/persona.py

"""
Module: chess.persona.persona
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from enum import Enum
from typing import List, Optional

from chess.geometry import Quadrant
from chess.vector import Vector


class Persona(Enum):
    """
    # ROLE: Build Configuration Table, Persona, Metadata Set

    # ABOUT THE PERSONA:
    The Persona implements a hashtable of attributes assigned to concrete Rank classes. The Rank's title is the hash
    key.

    ## STRUCTURE OF THE PERSONA HASHTABLE:
        *   Key (str)
        *   Value   (List{str: Any})

    ### Persona Value: List[{str: Any}] each tuple in the list represents {Persona.Entry.attribute: attribute_value}

    ## WHO USES THE PERSONA TABLE:
        *   RankBuilder uses a Persona.ELEMENT/ENTRY to create a Rank object.

    # RESPONSIBILITIES:
    1.  Metadata for each Rank.
    1.  Supply build parameters to RankFactory methods.

    # PARENT:
        *   Enum

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   designation (str)
        *   quota (int)
        *   ransom (int)
        *   quadrants (List[Quadrant])

    # INHERITED ATTRIBUTES:
        * name (str) -->  Name give to each Enum entry.
    """
    
    def __new__(
            cls,
            designation: str,
            quota: int,
            ransom: int,
            quadrants: List[Quadrant],
            vectors: Optional[List[Vector]]
    ):
        obj = object.__new__(cls)
        obj._designation = designation
        obj._quota = quota
        obj._ransom = ransom
        obj._quadrants = quadrants
        obj._vectors = vectors
        return obj
    
    PAWN = ("P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW], None)
    BISHOP = ("B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW], None)
    ROOK = ("C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W], None)
    KNIGHT = ("N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW],
              [
                  Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2), Vector(2, 1),
                  Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
              ]
    )
    KING = (
        "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW],
        [
            Vector(1, 0), Vector(-1, 0), Vector(0, 1), Vector(1, 1), Vector(-1, 1),
            Vector(-1, -1), Vector(1, -1)
        ]
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
        return self._quota
    
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
            f"per_rank:{self._quota} "
            f"value:{self._ransom} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )
    
    def quadrants_str(self) -> str:
        return " ".join(q.name for q in self._quadrants)

    # @classmethod
    # def find_speck_by_rank(cls, rank: Rank) -> Optional[Persona]:
    #     print(f"Looking for config with designation:{rank.visitor_name}")
    #
    #     for spec in Persona:
    #         print(f"Checking config:{spec.ransom}")
    #         if spec.designation.upper() == rank.visitor_name.upper():
    #             return spec
    #     return None
