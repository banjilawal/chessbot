# src/space/offset/quadrant/southeast/space.py

"""
Module: space.offset.quadrant.southeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import SoutheastQuadrantStepper
from space import QuadrantTraversalPattern


class SoutheastTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors southeast of the origin.

    Attributes:
        stepper: Optional[SoutheastQuadrantStepper]

    Provides:

    Super Class:
        QuadrantTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[SoutheastQuadrantStepper] | None = SoutheastQuadrantStepper(),
    ):
        """
        Args:
            stepper: Optional[SoutheastQuadrantStepper]
        """
        super().__init__(stepper=stepper)
        

    @property
    def stepper(self) -> SoutheastQuadrantStepper:
        return cast(SoutheastQuadrantStepper, self.stepper)

        
    