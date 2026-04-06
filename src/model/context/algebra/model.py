# src/model/context/algebra/model.py

"""
Module: model.context.algebra.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



from typing import Any, Dict, Optional


class AlgebraAcontext:
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Algebra attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            vector: Optional[Vector] = None,
            coord: Optional[Coord] = None,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
        """
        self._vector = vector
        self._coord = coord
        
    @property
    def vector(self) -> Optional[Vector]:
        return self._vector
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "coord": self._coord,
        }