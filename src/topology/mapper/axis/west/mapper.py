# src/topology/mapper/axis/west/mapper.py

"""
Module: topology.mapper.axis.west.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from topology.mapper import AxisMappingFunction
from domain.model import Vector
from domain.schema import AxisDelta
from topology.space import WestAxis



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