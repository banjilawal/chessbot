# src/geometry/mapper/axis/west/mapper.py

"""
Module: geometry.mapper.axis.west.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from geometry.mapper import AxisMappingFunction
from model import Vector
from schema import AxisDelta
from geometry.space import WestAxis



class WestAxisMapFunction(AxisMappingFunction[WestAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on west of origin.
            
    Attributes:
        delta: Vector = AxisMapFunction.WEST.vecto

    Provides:

    Super Class:
        AxisMapFunction
    """
    
    def __init__(self, delta: Vector = AxisDelta.WEST.vector):
        """
        Args:
            delta: Vector = AxisMapFunction.WEST.vector
        """
        super().__init__(delta=delta)