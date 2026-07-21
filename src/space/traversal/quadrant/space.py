# src/space/offset/quadrant/space.py

"""
Module: space.offset.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from math import QuadrantStepper
from space import TraversalPattern


class QuadrantTraversalPattern(TraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a bounded linear function from 2D space.
        2.  Provide the next point in the direction of travel.

    Attributes:
        stepper: QuadrantStepper

    Provides:

    Super Class:
        TraversalPattern
    """    
    def __init__(self, stepper: QuadrantStepper,):
        """
        Args:
            stepper: QuadrantStepper
        """
        super().__init__(stepper=stepper)
        
    @property
    def stepper(self) -> QuadrantStepper:
        return cast(QuadrantStepper, self.stepper)

        
    