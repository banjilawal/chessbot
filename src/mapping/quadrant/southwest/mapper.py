# src/mapping/quadrant/southwest/mapping.py

"""
Module: mapping.quadrant.southwest.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import QuadrantMapFunction
from schema import QuadrantStepFunction
from space import SouthwestQuadrant



class SouthwestMapFunction(QuadrantMapFunction[SouthwestQuadrant]):
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
        QuadrantMapFunction
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