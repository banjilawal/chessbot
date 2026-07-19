# src/space/stepper/axis/south/linear.py

"""
Module: space.stepper.axis.south.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from schema import AxisDelta
from space import AxisStepper


class SouthAxisStepper(AxisStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce the next vector on axis south of the origin.

    Attributes:
        delta: Vector

    Provides:

    Super Class:
        AxisStepper
    """

    
    def __init__(self, delta: Vector = AxisDelta.SOUTH.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)

        