# src/mapping/quadrant/northeast/mapping.py

"""
Module: mapping.quadrant.northeast.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import QuadrantMapFunction
from schema import QuadrantStepFunction
from space import NortheastQuadrant



class NortheastMapFunction(QuadrantMapFunction[NortheastQuadrant]):
    """
    Role:
        -   Computation
        -   Integrity Assurance

    Responsibilities:
        Define x_step and slope for getting the next vector northeast of origin.
            -   x_step = -1,
            -   slope = 1
            
    Attributes:
        x_step: int = QuadrantStepFunction.NORTHEAST.x_step,
        slope: int = QuadrantStepFunction.NORTHEAST.slope

    Provides:

    Super Class:
        QuadrantMapFunction
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.NORTHEAST.x_step,
            slope: int = QuadrantStepFunction.NORTHEAST.slope,
    ):
        """
        Args:
            x_step: int = QuadrantStepFunction.NORTHEAST.x_step
            slope: int = QuadrantStepFunction.NORTHEAST.slope
        """
        super().__init__(x_step=x_step, slope=slope)