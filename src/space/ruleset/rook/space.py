# src/space/ruleset/rook/space.py

"""
Module: space.ruleset.rook.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Rook, Vector
from space import TraversalRuleset


class RookTraversalRuleset(TraversalRuleset[Rook]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a RookBasis. Necessary for computing a RookToken's destination vectors.

    Attributes:
        maneuver_vectors: VectorSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self,):
        """
        Args:t
        """
        super().__init__(
            maneuver_vectors=VectorSet(
                    (
                        Vector(1, 0), Vector(-1, 0), Vector(0, 1),
                        Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)
                    )
            )
        )
    
