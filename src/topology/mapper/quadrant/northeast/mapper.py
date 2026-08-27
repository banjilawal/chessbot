# src/topology/mapper/quadrant/northeast/mapper.py

"""
Module: topology.mapper.quadrant.northeast.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from topology.mapper import QuadrantMappingFunction
from domain.schema import QuadrantStepFunction
from topology.space import NortheastQuadrant



class NortheastQuadrantMappingFunction(QuadrantMappingFunction[NortheastQuadrant]):
    """
    Role:
        - Computation
        -  Integrity Assurance

    Responsibilities:
        Define x_step and slope for getting the next vector northeast of origin.
            -  x_step = -1,
            -  slope = 1
            
    Attributes:
        x_step: int = QuadrantStepFunction.NORTHEAST.x_step,
        slope: int = QuadrantStepFunction.NORTHEAST.slope

    Provides:

    Super Class:
        QuadrantMappingFunction
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.NORTHEAST.x_step,
            slope: int = QuadrantStepFunction.NORTHEAST.slope,
    ):
        """
        Args:
            x_step: int = QuadrantStepFunction.NORTHEAST.x_step
            slope: int = QuadrantStepFunction.NORTHEAST.slope
        """
        super().__init__(x_step=x_step, slope=slope)