# src/logic/span/square/span.py

"""
Module: logic.span.square.span
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.square import Square
from logic.span import SquareRay


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
    
    def __init__(self, origin: Square, rays: List[SquareRay]):
        super().__init__(origin=origin, rays=rays)

    @property
    def origin(self) -> Square:
        return cast(Square, self.origin)
    
    @property
    def rays(self) -> List[SquareRay]:
        return cast(List[SquareRay], self.rays)