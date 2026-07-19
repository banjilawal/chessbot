# src/space/stepper/quadrant/space.py

"""
Module: space.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from space import QuadrantStepper


class SouthwestQuadrantStepper(QuadrantStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        QuadrantStepper for going northeast toward bottom left corner (0, num_columns - 1)
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
        super().__init__()