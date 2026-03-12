# src/logic/span/square/span.py

"""
Module: logic.span.square.span
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.square import Square
from logic.span import CoordRay, SquareRay


class SquareSpan:
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores rays projected from a common origin.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: Square
        *   rays: List[RAy]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Square
        *   rays: List[RAy]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    _origin: Square
    _rays: List[SquareRay]
    
    def __init__(self, origin: Square, rays: List[SquareRay]):
        self._origin = origin
        self._rays = rays
    
    @property
    def length(self) -> int:
        return len(self._rays)
    
    @property
    def origin(self) -> Square:
        return self._origin
    
    @property
    def rays(self) -> List[SquareRay]:
        return self._rays