# src/logic/span/coord/span.py

"""
Module: logic.span.coord.span
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.coord import Coord
from logic.span import Span
from logic.span.coord import CoordRay


class CoordSpan(Span[Coord]):
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores rays projected from a common Coord.

    # PARENT:
        *   Span

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        * See Span class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Coord
        *   rays: List[Ray[Coord]]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        * See Span class for inherited methods.
    """
    
    def __init__(self, origin: Coord, rays: List[CoordRay], sub_span_roots: List[Coord]):
        """
        Args:
            origin: Coord
            rays: List[CoordRay]
        """
        super().__init__(origin=origin, rays=rays)
        
    @property
    def origin(self) -> Coord:
        return cast(Coord, self.origin)
    
    @property
    def rays(self) -> List[CoordRay]:
        return cast(List[CoordRay], self.rays)
    
    @property
    def sub_span_roots(self) -> List[Coord]:
        return cast(List[Coord], self.sub_span_roots)
        
    