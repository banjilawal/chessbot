# src/logic/span/ray/perpendicular/provider/provider.py

"""
Module: logic.span.ray/perpendicular.provider.provider
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations

from logic.span import PerpendicularRayComputer, PerpendicularPlaneFactors


class PerpendicularRayProvider:
    """
    # ROLE: Utility
    # TASK: Provide solution sets

    # RESPONSIBILITIES:
    1.  Aggregate modules for computing components of perpendicular span from an origin.
    2.  Simplify CoordSpan derivations.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
            plane: PerpendicularPlaneFactors
            computer: PerpendicularRayComputer

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
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
    