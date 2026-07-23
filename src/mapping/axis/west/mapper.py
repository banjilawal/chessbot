# src/mapping/axis/west/mapping.py

"""
Module: mapping.axis.west.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import AxialMapFunction
from model import Vector
from schema import AxialDelta
from space import WestAxis



class WestAxisMapFunction(AxialMapFunction[WestAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on west of origin.
            
    Attributes:
        delta: Vector = AxialMapFunction.WEST.vecto

    Provides:

    Super Class:
        AxialMapFunction
    """
    
    def __init__(self, delta: Vector = AxialDelta.WEST.vector):
        """
        Args:
            delta: Vector = AxialMapFunction.WEST.vector
        """
        super().__init__(delta=delta)