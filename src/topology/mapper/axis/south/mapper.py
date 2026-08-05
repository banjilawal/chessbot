# src/topology/mapper/axis/south/mapper.py

"""
Module: topology.mapper.axis.south.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from topology.mapper import AxisMappingFunction
from model import Vector
from schema import AxisDelta
from topology.space import SouthAxis



class SouthAxisMapFunction(AxisMappingFunction[SouthAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on south of origin.
            
    Attributes:
        delta: Vector = AxisMapFunction.SOUTH.vecto

    Provides:

    Super Class:
        AxisMapFunction
    """
    
    def __init__(self, delta: Vector = AxisDelta.SOUTH.vector):
        """
        Args:
            delta: Vector = AxisMapFunction.SOUTH.vector
        """
        super().__init__(delta=delta)