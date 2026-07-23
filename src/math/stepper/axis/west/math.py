# src/math/stepper/axis/west/math.py

"""
Module: math.stepper.axis.west.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from math import AxisStepper
from model import Vector
from schema import AxialDelta



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
        AxialMappingFunction
    """

    
    def __init__(self, delta: Vector = AxialDelta.WEST.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)

        