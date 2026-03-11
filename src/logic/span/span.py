# src/logic/span/span.py

"""
Module: logic.span.span
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord
from logic.span import Ray

class Span:
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores rays projected from a common origin.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: Coord
        *   rays: List[RAy]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Coord
        *   rays: List[RAy]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    _origin: Coord
    _rays: List[Ray]
    
    def __init__(self, origin: Coord, rays: List[Ray]):
        self._origin = origin
        self._rays = rays
        
    @property
    def length(self) -> int:
        return len(self._rays)
    
    @property
    def origin(self) -> Coord:
        return self._origin
    
    @property
    def rays(self) -> List[Ray]:
        return self._rays
        
    