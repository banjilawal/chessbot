# src/math/stepper/quadrant/math.py

"""
Module: math.stepper.quadrant.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from schema import QuadrantStepFunction
from stepper import QuadrantStepper


class SouthwestQuadrantStepper(QuadrantStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        Define the x_step and slope to get nex x_step and slope for to QuadrantSteQuadrantStepper for going northeast toward bottom left corner (0, num_columns - 1)
            -   x_step = -1,
            -   slope = 1
            
    Attributes:

    Provides:

    Super Class:
        QuadrantStepper
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.SOUTHWEST.x_step,
            slope: int = QuadrantStepFunction.SOUTHWEST.slope,
    ):
        super().__init__(x_step=x_step, slope=slope)