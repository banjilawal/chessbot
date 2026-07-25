# src/space/offset/quadrant/southwest/space.py

"""
Module: space.offset.quadrant.southwest.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import SouthwestQuadrantStepper
from space import QuadrantTraversalPattern


class SouthwestTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors southwest of the origin.

    Attributes:
        stepper: Optional[SouthwestQuadrantStepper]

    Provides:

    Super Class:
        QuadrantTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[SouthwestQuadrantStepper] | None = SouthwestQuadrantStepper(),
    ):
        """
        Args:
            stepper: Optional[SouthwestQuadrantStepper]
        """
        super().__init__(stepper=stepper)
        

    @property
    def stepper(self) -> SouthwestQuadrantStepper:
        return cast(SouthwestQuadrantStepper, self.stepper)

        
    