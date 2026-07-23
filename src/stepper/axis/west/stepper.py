# src/stepper/axis/west/stepper.py

"""
Module: stepper.axis.west.stepper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from space import WestAxis
from stepper import AxialDelta


class WestAxisDelta(AxialDelta[WestAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on west of origin.
            
    Attributes:
        delta: Vector

    Provides:

    Super Class:
        AxialDelta
    """
    
    def __init__(self, delta: Vector = AxialDelta):
        """
        Args:
            origin: Vector,
            delta: Vector = AxialDelta.WEST.vector
        """
        super().__init__(delta=delta)