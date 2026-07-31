# src/geometry/mapper/quadrant/southeast/mapper.py

"""
Module: geometry.mapper.quadrant.southeast.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from geometry.mapper import QuadrantMappingFunction
from schema import QuadrantStepFunction
from geometry.space import SoutheastQuadrant



class SoutheastQuadrantMappingFunction(QuadrantMappingFunction[SoutheastQuadrant]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define x_step and slope for getting the next vector southeast of origin.
            -   x_step = -1,
            -   slope = 1
            
    Attributes:
        x_step: int = QuadrantStepFunction.SOUTHEAST.x_step,
        slope: int = QuadrantStepFunction.SOUTHEAST.slope

    Provides:

    Super Class:
        QuadrantMappingFunction
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.SOUTHEAST.x_step,
            slope: int = QuadrantStepFunction.SOUTHEAST.slope,
    ):
        """
        Args:
            x_step: int = QuadrantStepFunction.SOUTHEAST.x_step
            slope: int = QuadrantStepFunction.SOUTHEAST.slope
        """
        super().__init__(x_step=x_step, slope=slope)