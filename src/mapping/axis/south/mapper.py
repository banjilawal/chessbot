# src/mapping/axis/south/mapping.py

"""
Module: mapping.axis.south.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import AxialMappingFunction
from model import Vector
from schema import AxialDelta
from space import SouthAxis



class SouthAxisMapper(AxialMappingFunction[SouthAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on south of origin.
            
    Attributes:
        delta: Vector = AxialMappingFunction.SOUTH.vecto

    Provides:

    Super Class:
        AxialMappingFunction
    """
    
    def __init__(self, delta: Vector = AxialDelta.SOUTH.vector):
        """
        Args:
            delta: Vector = AxialMappingFunction.SOUTH.vector
        """
        super().__init__(delta=delta)