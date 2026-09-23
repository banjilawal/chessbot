# src/domain/structure/toggle/vector/toggle.py

"""
Module: domain.structure.toggle.vector.toggle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from domain import Locus, Coord, Model, Toggle, Vector


class Cartesian(Model):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Picks selector a
                - Coord Geometric quantity
                - Vector: Linear Vector
            as an selector for multiplication, conversion or simple addition.

    Attributes:
        locus: Optional[Coord | Vector]
        size: int

    Provides:
        is_coord_locus: bool
        is_vector_locus: bool
        to_dict: Dict[str: Any]

    Super Class:
        Model
    """
    _coord: Optional[Coord]
    _vector: Optional[Vector]

    
    def __init__(
            self,
            coord: Optional[Coord] | None = None,
            vector: Optional[Vector] | None = None,
    ):
        """
        Args:
            coord: Optional[Coord]
            vector: Optional[Vector]
        """
        super().__init__()
        self._vector = vector
        self._coord = coord
        
    @property
    def locus(self) -> Optional[Coord | Vector]:
        if self._vector is None and self._coord is None:
            return None
        if self._vector:
            return self._vector
        return self._coord
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "coord": self._coord,
        }
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_coord_locus(self) -> bool:
        if self.is_empty:
            return False
        return (
                self._vector is None and
                self._coord is not None and
                isinstance(self._coord, Coord)
        )
    
    @property
    def is_vector_locus(self) -> bool:
        if self.is_empty:
            return False
        return (
                self._vector is not None and
                self._coord is None and
                isinstance(self._vector, Vector)
        )
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def has_excess_loci(self) -> bool:
        return self.size > 1

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Cartesian):
            if other.is_vector_locus:
                return self._equal_vector_loci(other)
            return self._equal_coord_loci(other)
        return False
        
    def _equal_vector_loci(self, other: Cartesian) -> bool:
        if self.is_vector_locus and other.is_vector_locus:
            return self.locus == other.locus
        return False
    
    def _equal_coord_loci(self, other: Cartesian) -> bool:
        if self.is_coord_locus and other.is_coord_locus:
            return self.locus == other.locus
        return False
    
    