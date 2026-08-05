# src/topology/mapper/axis/east/mapper.py

"""
Module: topology.mapper.axis.east.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from topology.mapper import AxisMappingFunction
from model import Vector
from schema import AxisDelta
from topology.space import EastAxis



class EastAxisMapFunction(AxisMappingFunction[EastAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on east of origin.
            
    Attributes:
        delta: Vector = AxisMapFunction.EAST.vecto

    Provides:

    Super Class:
        AxisMapFunction
    """
    
    def __init__(self, delta: Vector = AxisDelta.EAST.vector):
        """
        Args:
            delta: Vector = AxisMapFunction.EAST.vector
        """
        super().__init__(delta=delta)