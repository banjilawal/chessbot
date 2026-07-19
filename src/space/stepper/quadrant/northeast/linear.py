# src/space/stepper/quadrant/space.py

"""
Module: space.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from schema import QuadrantStepFunction
from space import QuadrantStepper


class NortheastQuadrantStepper(QuadrantStepper):
    """
    Role:
        -   Computation Worker
        
    Responsibilities:
        QuadrantStepper for going northeast toward top left corner (0, 0)
            -   x_step = -1,
            -   slope = -1

    Attributes:

    Provides:

    Super Class:
        QuadrantStepper
    """
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.NORTHEAST.x_step,
            slope: int = QuadrantStepFunction.NORTHEAST.slope,
    ):
        super().__init__(x_step=x_step, slope=slope)
