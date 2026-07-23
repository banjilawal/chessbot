# src/math/stepper/axis/south/math.py

"""
Module: math.stepper.axis.south.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from math import AxisStepper
from model import Vector
from schema import AxialDelta



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
        AxialMapFunction
    """

    
    def __init__(self, delta: Vector = AxialDelta.SOUTH.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)

        