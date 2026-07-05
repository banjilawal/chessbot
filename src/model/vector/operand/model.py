# src/model/vector/register/category.py

"""
Module: model.vector.operand.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Coord, Model, OperandCategory, Vector


class VectorOperand(Model):
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
        is_coord: bool
        is_vector: bool
        category: OperandCategory
        to_dict: Dict[str, Any]

    Provides:

    Super Class:
        Model
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    _category: Optional[OperandCategory] = OperandCategory.NOT_INITIALIZED
    
    def __init__(
            self,
            vector: Optional[Vector] | None = None,
            coord: Optional[Coord] | None = None,
            category: Optional[OperandCategory] | None = None,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
        """
        self._vector = vector
        self._coord = coord
        self._category = category
        
    @property
    def vector(self) -> Optional[Vector]:
        return self._vector
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def category(self) -> OperandCategory:
        return self._category
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "coord": self._coord,
        }
    
    @property
    def is_coord(self) -> bool:
        return (
                self._vector is None and
                self._coord is not None and
                isinstance(self._coord, Coord)
        )
    
    @property
    def is_vector(self) -> bool:
        return (
                self._vector is not None and
                self._coord is None and
                isinstance(self._vector, Vector)
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorOperand):
            return (
                    self._vector == other.vector and
                    self._coord == other.coord
            )