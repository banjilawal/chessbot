# src/mapping/axis/north/mapping.py

"""
Module: mapping.axis.north.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from mapping import AxialMapFunction
from model import Vector
from schema import AxialDelta
from space import NorthAxis



class NorthAxisMapFunction(AxialMapFunction[NorthAxis]):
    """
    Role:
        -   Computation

    Responsibilities:
        Define delta_vector for getting the next vector on north of origin.
            
    Attributes:
        delta: Vector = AxialMapFunction.NORTH.vecto

    Provides:

    Super Class:
        AxialMapFunction
    """
    
    def __init__(self, delta: Vector = AxialDelta.NORTH.vector):
        """
        Args:
            delta: Vector = AxialMapFunction.NORTH.vector
        """
        super().__init__(delta=delta)