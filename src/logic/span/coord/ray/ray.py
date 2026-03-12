# src/logic/span/coord/ray/ray.py

"""
Module: logic.span.coord.ray.ray
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.span import Ray
from logic.coord import Coord

class CoordRay(Ray[Coord]):
    """
    # ROLE: Data-Holder
    
    # RESPONSIBILITIES:
    1.  Stores members that define a ray from an origin to a terminus

    # PARENT:
        *   Ray

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Ray class for inherited attributes

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Coord
        *   members: List[Coord]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See Ray class for inherited methods
    """
    
    def __init__(self, origin: Coord, members: List[Coord]):
        """
        Args:
            origin: Coord
            members: List[Coord]
        """
        super().__init__(origin=origin, members=members)
        
    @property
    def origin(self) -> Coord:
        return cast(Coord, self.origin)
    
    @property
    def members(self) -> List[Coord]:
        return cast(List[Coord], self.members)