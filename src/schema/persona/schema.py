# src/schema/persona/schema.py

"""
Module: schema.persona.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from model import OldQuadrant, Vector


class Persona(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set
        

    Responsibilities:
        1.  Supply parameters to Token builders and factories.
    
    Attributes:
        quota: int
        ransom: int
        designation: str
        quadrants: List[Quadrant]
        vectors: Optional[List[Vector]]

    Super Class:
        Enum

    About:
        The Persona implements a hashtable of attributes assigned to concrete Rank classes.
        The Rank's title is the hash key.

    ## STRUCTURE OF THE PERSONA HASHTABLE:
        *   Key (str)
        *   Value   (List{str: Any})

    ### Persona Value: List[{str: Any}] each tuple in the list represents {Persona.Entry.attribute: attribute_value}

    ## WHO USES THE PERSONA TABLE:
        *   RankBuilder uses a Persona.ELEMENT/ENTRY to create a Rank object.
    """
    
    def __new__(
            cls,
            designation: str,
            quota: int,
            ransom: int,
            quadrants: List[OldQuadrant],
            vectors: Optional[List[Vector]]
    ):
        """
        Args:
            designation: str
            quota: int
            ransom: int
            quadrants: List[Quadrant]
            vectors: Optional[List[Vector]]
        """
        obj = object.__new__(cls)
        obj._designation = designation
        obj._quota = quota
        obj._ransom = ransom
        obj._quadrants = quadrants
        obj._vectors = vectors
        return obj
    
    PAWN = ("P", 8, 1, [OldQuadrant.NE, OldQuadrant.SE, OldQuadrant.NW, OldQuadrant.SW], None)
    BISHOP = ("B", 2, 3, [OldQuadrant.NE, OldQuadrant.NW, OldQuadrant.SE, OldQuadrant.SW], None)
    ROOK = ("C", 2, 5, [OldQuadrant.N, OldQuadrant.S, OldQuadrant.E, OldQuadrant.W], None)
    KNIGHT = ("N", 2, 3, [OldQuadrant.N, OldQuadrant.NE, OldQuadrant.NW, OldQuadrant.E, OldQuadrant.SE, OldQuadrant.SW],
              [
                  Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2), Vector(2, 1),
                  Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
              ]
    )
    KING = (
        "K", 1, 0,
        [OldQuadrant.N, OldQuadrant.NE, OldQuadrant.E, OldQuadrant.SE, OldQuadrant.S, OldQuadrant.SW, OldQuadrant.W, OldQuadrant.NW],
        [
            Vector(1, 0), Vector(-1, 0), Vector(0, 1), Vector(1, 1), Vector(-1, 1),
            Vector(-1, -1), Vector(1, -1)
        ]
    )
    QUEEN = (
        "Q", 1, 9,
        [OldQuadrant.N, OldQuadrant.NE, OldQuadrant.E, OldQuadrant.SE, OldQuadrant.S, OldQuadrant.SW, OldQuadrant.W, OldQuadrant.NW]
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
    def quadrants(self) -> List[OldQuadrant]:
        return self._quadrants
    
    @property
    def vectors(self) -> List[Vector]:
        return self._vectors
    
    @classmethod
    def allowed_quadrants(cls) -> List[List[OldQuadrant]]:
        return [member.quadrants for member in cls]
    
    def __str__(self) -> str:
        return (
            f"Rank["
            f"{self._designation} "
            f"per_rank:{self._quota} "
            f"value:{self._ransom} "
            f"quadrants:({len(self.quadrants_str())})"
            f"] "
        )
    
    def quadrants_str(self) -> str:
        return " ".join(q.name for q in self._quadrants)

