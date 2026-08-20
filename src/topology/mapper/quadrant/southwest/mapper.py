# src/topology/mapper/quadrant/southwest/mapper.py

"""
Module: topology.mapper.quadrant.southwest.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from topology.mapper import QuadrantMappingFunction
from schema import QuadrantStepFunction
from topology.space import SouthwestQuadrant



class SouthwestQuadrantMappingFunction(QuadrantMappingFunction[SouthwestQuadrant]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define x_step and slope for getting the next vector southwest of origin.
            -   x_step = -1,
            -   slope = 1
            
    Attributes:
        x_step: int = QuadrantStepFunction.SOUTHWEST.x_step,
        slope: int = QuadrantStepFunction.SOUTHWEST.slope

    Provides:

    Super Class:
        QuadrantMappingFunction
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.SOUTHWEST.x_step,
            slope: int = QuadrantStepFunction.SOUTHWEST.slope,
    ):
        """
        Args:
            x_step: int = QuadrantStepFunction.SOUTHWEST.x_step
            slope: int = QuadrantStepFunction.SOUTHWEST.slope
        """
        super().__init__(x_step=x_step, slope=slope)