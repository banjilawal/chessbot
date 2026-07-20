# src/math/stepper/axis/west/linear.py

"""
Module: math.stepper.axis.west.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from schema import AxisDelta
from space import AxisStepper


class WestAxisStepper(AxisStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce the next vector on axis west of the origin.

    Attributes:
        delta: Vector

    Provides:

    Super Class:
        AxisStepper
    """

    
    def __init__(self, delta: Vector = AxisDelta.WEST.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)

        