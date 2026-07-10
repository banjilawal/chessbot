# src/model.point/model.py

"""
Module: model.point.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Coord, Vector


class Point:
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks either a
                -   Coord: Geometric quantity
                -   Vector: Linear Vector
            as an operand for multiplication, conversion or simple addition.

    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]
        is_coord_point: bool
        is_vector_point: bool
        is_empty_point: bool
        is_conflicting_point: bool
        to_dict: Dict[str, Any]

    Provides:

    Super Class:
        Operand
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            vector: Optional[Vector] | None = None,
            coord: Optional[Coord] | None = None,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
        """
        self._vector = vector
        self._coord = coord
        
    @property
    def operand(self) -> Optional[Coord|Vector]:
        return self._vector or self._coord
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "coord": self._coord,
        }
    
    @property
    def is_coord_point(self) -> bool:
        return (
                self._vector is None and
                self._coord is not None and
                isinstance(self._coord, Coord)
        )
    
    @property
    def is_vector_point(self) -> bool:
        return (
                self._vector is not None and
                self._coord is None and
                isinstance(self._vector, Vector)
        )
    
    @property
    def is_empty_point(self) -> bool:
        return self._vector is None and self._coord is None
    
    @property
    def is_conflicting_point(self) -> bool:
        return self._vector is not None and self._coord is not None
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Point):
            return (
                    self._vector == other.vector and
                    self._coord == other.coord
            )