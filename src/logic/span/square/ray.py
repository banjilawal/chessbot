# src/logic/span/square/ray.py

"""
Module: logic.span.square.ray
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.square import Square


class SquareRay:
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores points that define a ray from an origin to a terminus

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: Square
        *   points: List[Square]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Square
        *   points: List[Square]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    _origin: Square
    _points: List[Square]
    
    def __init__(self, origin: Square, points: List[Square]):
        """
        Args:
            origin: Square
            points: List[Square]
        """
        self._origin = origin
        self._points = points
    
    @property
    def origin(self) -> Square:
        return self._origin
    
    @property
    def points(self) -> List[Square]:
        return self._points
    
    @property
    def origin_inclusive_length(self) -> int:
        return len(self._points) + 1