# src/topology/mapper/axis/north/mapper.py

"""
Module: topology.mapper.axis.north.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from topology.mapper import AxisMappingFunction
from domain.model import Vector
from domain.schema import AxisDelta
from topology.space import NorthAxis



class NorthAxisMapFunction(AxisMappingFunction[NorthAxis]):
    """
    Role:
        - Computation

    Responsibilities:
        Define delta_vector for getting the next vector on north of origin.
            
    Attributes:
        delta: Vector = AxisMapFunction.NORTH.vecto

    Provides:

    Super Class:
        AxisMapFunction
    """
    
    def __init__(self, delta: Vector = AxisDelta.NORTH.vector):
        """
        Args:
            delta: Vector = AxisMapFunction.NORTH.vector
        """
        super().__init__(delta=delta)