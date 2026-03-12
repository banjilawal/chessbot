# src/logic/span/coord/ray/diagonal/provider/provider.py

"""
Module: logic.span.coord.ray.diagonal.provider.provider
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations

from logic.span import DiagonalRayComputer, DiagonalPlaneFactors


class DiagonalRayProvider:
    """
    # ROLE: Utility
    # TASK: Provide solution sets

    # RESPONSIBILITIES:
    1.  Aggregate modules for computing components of diagonal span from an origin.
    2.  Simplify CoordSpan derivations.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
            plane: DiagonalPlaneFactors
            computer: DiagonalRayComputer

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
            plane: DiagonalPlaneFactors
            computer: DiagonalRayComputer

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _plane: DiagonalPlaneFactors
    _computer: DiagonalRayComputer
    
    def __init__(
            self,
            plane: DiagonalPlaneFactors = DiagonalPlaneFactors(),
            computer: DiagonalRayComputer = DiagonalRayComputer(),
    ):
        """
        Args:
            plane: DiagonalPlaneFactors
            computer: DiagonalRayComputer
        """
        self._plane = plane
        self._computer = computer
        
    @property
    def factors(self) -> DiagonalPlaneFactors:
        return self._plane
    
    @property
    def ray(self) -> DiagonalRayComputer:
        return self._computer
    