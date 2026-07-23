# src/mapping/axis/east/mapping.py

"""
Module: mapping.axis.east.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import AxialMapFunction
from model import Vector
from schema import AxialDelta
from space import EastAxis



class EastAxisMapFunction(AxialMapFunction[EastAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on east of origin.
            
    Attributes:
        delta: Vector = AxialMapFunction.EAST.vecto

    Provides:

    Super Class:
        AxialMapFunction
    """
    
    def __init__(self, delta: Vector = AxialDelta.EAST.vector):
        """
        Args:
            delta: Vector = AxialMapFunction.EAST.vector
        """
        super().__init__(delta=delta)