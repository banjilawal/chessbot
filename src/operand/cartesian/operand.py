# src/operand/cartesian/operand.py

"""
Module: operand.cartesian.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional, cast

from model import Coord, Vector
from operand import Operand


class CartesianOperand(Operand):
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
        entity: Optional[Coord|Vector]
        is_coord_point: bool
        is_vector_point: bool

    Provides:
        
        -   _equal_vector_points(point: Point) -> bool
        -  _equal_coord_points(self, point: Point) -> bool
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
        super().__init__()
        self._vector = vector
        self._coord = coord
        
    @property
    def entity(self) -> Optional[Coord|Vector]:
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
    def is_empty(self) -> bool:
        return len(self.to_dict) == 0
    
    @property
    def is_full(self) -> bool:
        return len(self.to_dict) == 1
    
    @property
    def has_overflow(self) -> bool:
        return len(self.to_dict) >= 2
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CartesianOperand):
            point = cast(CartesianOperand, other)
            if point.is_vector_point:
                return self._equal_vector_points(point)
            return self._equal_coord_points(self)
        return False
        
    def _equal_vector_points(self, point: CartesianOperand) -> bool:
        if self.is_vector_point and point.is_vector_point:
            return self.entity == point.entity
        return False
    
    def _equal_coord_points(self, point: CartesianOperand) -> bool:
        if self.is_coord_point and point.is_coord_point:
            return self.entity == point.entity
        return False
    
    