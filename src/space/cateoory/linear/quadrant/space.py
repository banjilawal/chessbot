# src/space/linear/quadrant/space.py

"""
Module: space.linear.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from register import VectorRegister
from space import LinearSpace, QuadrantStepper


class Quadrant(LinearSpace):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a bounded linear function from 2D space.
        2.  Provide the next point in the direction of travel.

    Attributes:
        endpoints: VectorRegister
        stepper: QuadrantStepper

    Provides:

    Super Class:
        LinearSpace
    """    
    def __init__(self, endpoints: VectorRegister, stepper: QuadrantStepper,):
        """
        Args:
            endpoints: QuadrantBounds
            stepper: QuadrantStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        
    @property
    def stepper(self) -> QuadrantStepper:
        return cast(QuadrantStepper, self.stepper)
        
    