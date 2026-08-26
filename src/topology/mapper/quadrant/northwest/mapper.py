# src/topology/mapper/quadrant/northwest/mapper.py

"""
Module: topology.mapper.quadrant.northwest.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.schema import QuadrantStepFunction
from topology.space import NorthwestQuadrant



class NorthwestQuadrantMappingFunction(QuadrantMappingFunction[NorthwestQuadrant]):
    """
    Role:
        -  Computation

    Responsibilities:
        Define x_step and slope for getting the next vector northwest of origin.
            -  x_step = -1,
            -  slope = 1
            
    Attributes:
        x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
        slope: int = QuadrantStepFunction.NORTHWEST.slope

    Provides:

    Super Class:
        QuadrantMappingFunction
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
            slope: int = QuadrantStepFunction.NORTHWEST.slope,
    ):
        """
        Args:
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step
            slope: int = QuadrantStepFunction.NORTHWEST.slope
        """
        super().__init__(x_step=x_step, slope=slope)