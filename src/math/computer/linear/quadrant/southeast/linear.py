# src/math/stepper/quadrant/math.py

"""
Module: math.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from schema import QuadrantStepFunction
from space import QuadrantStepper


class SoutheastQuadrantStepper(QuadrantStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
    QuadrantStepper for going northeast toward bottom right corner (num_rows - 1, num_columns - 1)
        -   x_step = 1,
        -   slope = 1
    Attributes:

    Provides:

    Super Class:
        QuadrantStepper
    """
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.SOUTHEAST.x_step,
            slope: int = QuadrantStepFunction.SOUTHEAST.slope,
    ):
        super().__init__(x_step=x_step, slope=slope)