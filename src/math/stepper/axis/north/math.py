# src/math/stepper/axis/north/math.py

"""
Module: math.stepper.axis.north.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from schema import AxisDelta
from space import AxisStepper


class NorthAxisStepper(AxisStepper):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce the next vector on axis north of the origin.

    Attributes:
        delta: Vector

    Provides:

    Super Class:
        AxisStepper
    """

    
    def __init__(self, delta: Vector = AxisDelta.NORTH.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)

        