# src/model/context/vector/model.py

"""
Module: model.context.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Coord, OperandCategory, Vector


class VectorOperand:
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks either a
                -   Coord: Geometric quantity
                -   Vector: Linear Vectoric
            as an operand for multiplication, conversion or simple addition.

    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    _category: OperandCategory = OperandCategory.NOT_INITIALIZED
    
    def __init__(
            self,
            vector: Optional[Vector] | None = None,
            coord: Optional[Coord] | None = None,
            category: OperandCategory | None = None,
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