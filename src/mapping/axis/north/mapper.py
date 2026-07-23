# src/mapping/axis/north/mapping.py

"""
Module: mapping.axis.north.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import AxialMappingFunction
from model import Vector
from schema import AxialDelta
from space import NorthAxis



class NorthAxisMapper(AxialMappingFunction[NorthAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on north of origin.
            
    Attributes:
        delta: Vector = AxialMappingFunction.NORTH.vecto

    Provides:

    Super Class:
        AxialMappingFunction
    """
    
    def __init__(self, delta: Vector = AxialDelta.NORTH.vector):
        """
        Args:
            delta: Vector = AxialMappingFunction.NORTH.vector
        """
        super().__init__(delta=delta)