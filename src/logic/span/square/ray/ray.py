# src/logic/span/square/ray.py

"""
Module: logic.span.square.ray
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.span import Ray
from logic.square import Square


class SquareRay(Ray[Square]):
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores members that define a ray from an origin to a terminus

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Square

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    def __init__(self, origin: Square, members: List[Square]):
        """
        Args:
            origin: Square
            members: List[Square]
        """
        super().__init__(origin=origin, members=members)
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.origin)
    
    @property
    def members(self) -> List[Square]:
        return cast(List[Square], self.members)