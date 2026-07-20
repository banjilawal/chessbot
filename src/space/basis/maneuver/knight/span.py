# src/space/span/maneuver/knight/span.py

"""
Module: space.span.maneuver.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Knight, Vector
from space import ManeuverVectorSet


class KnightManeuverVector(ManeuverVectorSet[Knight]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a KnightBasis. Necessary for computing a KnightToken's destination vectors.

    Attributes:
        maneuver_vectors: VectorSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self,):
        """
        """
        super().__init__(
            maneuver_vectors=VectorSet(
                (
                    Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
                    Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
                )
            )
        )
    
