# src/domain/structure/toggle/vector/toggle.py

"""
Module: domain.structure.toggle.vector.toggle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, Dict, Optional, cast

from domain import Cartesian, Toggle, Vector


class CartesianToggle(Toggle[Cartesian]):
    """
    Role:
        - Option Selector
        -   Data-Holder

    Responsibilities:
        1.  Picks selector a
                -   Cartesian: Geometric quantity
                -   Vector: Linear Vector
            as an selector for multiplication, conversion or simple addition.

    Attributes:
        vector: Optional[Vector]
        cartesian: Optional[Cartesian]
        entity: Optional[Cartesian|Vector]
        is_cartesian_point: bool
        is_vector_point: bool

    Provides:
        
        -   equal_vector_points(point: Point) -> bool
        -   equal_cartesian_points(self, point: Point) -> bool
        
    Super Class:
        Toggle
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
    def entity(self) -> Optional[Coord | Vector]:
        return self._vector or self._coord
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "cartesian": self._coord,
        }
    
    @property
    def switched_cartesian_on(self) -> bool:
        return (
                self._vector is None and
                self._coord is not None and
                isinstance(self._coord, Cartesian)
        )
    
    @property
    def is_vector_selector(self) -> bool:
        return (
                self._vector is not None and
                self._coord is None and
                isinstance(self._vector, Vector)
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CartesianToggle):
            point = cast(CartesianToggle, other)
            if point.is_vector_selector:
                return self._equal_vector_points(point)
            return self._equal_cartesian_points(self)
        return False
        
    def _equal_vector_points(self, point: CartesianToggle) -> bool:
        if self.is_vector_selector and point.is_vector_selector:
            return self.entity == point.entity
        return False
    
    def _equal_cartesian_points(self, point: CartesianToggle) -> bool:
        if self.switched_cartesian_on and point.switched_cartesian_on:
            return self.entity == point.entity
        return False
    
    