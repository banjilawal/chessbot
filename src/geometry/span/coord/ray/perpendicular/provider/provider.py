# src/geometry/span/coord/ray/perpendicular/provider/provider.py

"""
Module: geometry.span.coord.ray.perpendicular.provider.provider
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations

from math.span import PerpendicularRayComputer, PerpendicularPlaneFactors


class PerpendicularRayProvider:
    """
    Role:Utility
    # TASK: Provide solution sets

    Responsibilities:
    1.  Aggregate modules for computing components of perpendicular span from an origin.
    2.  Simplify CoordSpan derivations.

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
            plane: PerpendicularPlaneFactors
            computer: PerpendicularRayComputer

    # INHERITED ATTRIBUTES:
    None

    Attributes:
            plane: PerpendicularPlaneFactors
            computer: PerpendicularRayComputer

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    def __init__(
            self,
            factors: PerpendicularPlaneFactors = PerpendicularPlaneFactors(),
            computer: PerpendicularRayComputer = PerpendicularRayComputer(),
    ):
        """
        Args:
            factors: PerpendicularPlaneFactors
            computer: PerpendicularRayComputer
        """
        self._factors= factors
        self._computer = computer
        
    @property
    def factors(self) -> PerpendicularPlaneFactors:
        return self._factors
    
    @property
    def ray(self) -> PerpendicularRayComputer:
        return self._computer
    